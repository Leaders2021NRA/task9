from pdf2image import convert_from_path
import os
#import comtypes.client

class XToJPEG:
    def __init__(self):
        
        #self.app_excel = comtypes.client.CreateObject('Excel.Application')
        #self.app_excel.Visible = False
        
        #self.app_word  = comtypes.client.CreateObject('Word.Application')
        #self.app_word.Visible = False
        
    def __del__(self):
        #self.app_excel.Quit()
        #self.app_word.Quit()
    
    def convert(self, file_path, output_dir):
        file_path_with_no_extension, file_extension = os.path.splitext(file_path)
        file_extension = file_extension.lower()

        # for some files we have to convert them to pdf first
        if file_extension != '.pdf':
            
            #file_path_pdf = f'{os.path.join(output_dir, os.path.splitext(os.path.basename(file_path))[0])}.pdf'
            # 
            #if file_extension in ('.xls', '.xlsx'):
            #    doc = self.app_excel.Workbooks.Open(file_path)
            #    doc.ExportAsFixedFormat(0, file_path_pdf, 1, 0)
            #    doc.Close()
            #elif file_extension in ('.doc', '.docx'):
            #    doc = self.app_word.Documents.Open(file_path)
            #    doc.SaveAs(file_path_pdf, 17)
            #    #doc.ExportAsFixedFormat(file_path_pdf, 17, False, 0, 1, True)
            #    doc.Close()
            #else:
            #    raise NotImplementedError(f'Unknown type {file_extension} in XToJPEG')
            raise NotImplementedError(f'Unknown type {file_extension} in XToJPEG')
            #file_path = file_path_pdf
        
        return self.convert_pdf_to_image(file_path, output_dir)
    
    def convert_pdf_to_image(self, file_path, output_dir):
        images = convert_from_path(file_path)

        for i in range(len(images)):   
            images[i].save(os.path.join(output_dir, f'page{i}.jpg'), 'JPEG')