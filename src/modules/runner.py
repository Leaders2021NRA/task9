import cv2
import os
import datetime
import re
from matplotlib import pyplot as plt

from .ner import PersonExtractor
from .ocr import OCR
from .converters import XToJPEG

class Runner:
    def __init__(self):
        self.jpeg_converter = XToJPEG()
        self.ocr = OCR()
        self.person_extractor = PersonExtractor()

    def process(self, input_file_path, ouput_dir_path):
        
        # convert input file to jpeg
        self.jpeg_converter.convert(input_file_path, ouput_dir_path)
        
        # iterate over jpegs (1 jpg - 1 page in file)
        for file in os.listdir(ouput_dir_path):
            file_path = os.path.join(ouput_dir_path, file)
            
            # read image
            img = cv2.imread(file_path)
            
            # get OCR results
            ocr_result = self.ocr.process(file_path)

            # combine texts together
            text_combined_position2box_number = {}
            text_combined = ''
            curr_position = 0
            hyphenation_primitive_criterion = False

            for i, text in enumerate(ocr_result['text']):
                if text != '':        
                    if not hyphenation_primitive_criterion:
                        # we add space between words 
                        text_combined += ' '
                        curr_position += 1

                    # if prev word was on previos line we shell delete leading spaces for next word
                    if hyphenation_primitive_criterion:
                        text = text.lstrip()
                        hyphenation_primitive_criterion = False

                    if re.findall('[^\d][ ]*-[ ]*', text):
                        text = re.sub('[ ]*-[ ]*', '', text)
                        hyphenation_primitive_criterion = True

                    for j in range(len(text)):
                        text_combined_position2box_number[curr_position+j] = i
                    text_combined += text
                    curr_position += len(text)

            # get PER from combined text
            persons = self.person_extractor.get_persons(text_combined)

            # find out which boxes around text we should mark
            boxes_num_to_show = set() 
            for _, _, (i, j) in persons:
                for k in range(i, j+1):
                    if k in text_combined_position2box_number:
                        boxes_num_to_show.add(text_combined_position2box_number[k])

            # iterate over boxes and mark PER with red, other with green
            n_boxes = len(ocr_result['text'])
            for i in range(n_boxes):
                if int(float(ocr_result['conf'][i])) > 0: # TODO check threshold
                    (x, y, w, h) = (ocr_result['left'][i], 
                                    ocr_result['top'][i], 
                                    ocr_result['width'][i], 
                                    ocr_result['height'][i])

                    if i in boxes_num_to_show:
                        c = (0, 0, 255)
                    else:
                        c = (0, 255, 0)

                    img = cv2.rectangle(img, (x, y), (x + w, y + h), c, 2)


            # save reult in the same dir
            output_file = os.path.join(ouput_dir_path, f'{file.rsplit(".", 1)[0]}_res.jpg')
            cv2.imwrite(output_file, img)