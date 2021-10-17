from pdf2image import convert_from_path
import os

class XToJPEG:
    def __init__(self):
        pass
    
    def convert(self, file_path, output_dir):
        file_type = file_path.rsplit('.', 1)[1]
        
        if file_type == 'pdf':
            return self.convert_pdf_to_image(file_path, output_dir)
        else:
            raise NotImplementedError(f'Unknown type {file_type} in XToJPEG')
    
    def convert_pdf_to_image(self, file_path, output_dir):
        images = convert_from_path(file_path)

        for i in range(len(images)):   
            images[i].save(os.path.join(output_dir, f'page{i}.jpg'), 'JPEG')