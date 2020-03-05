import subprocess
import tempfile
import sys

class ChromePDF(object):

    # set headless chrome arguments
    _chrome_args = (
        '{chrome_exec}',
        '--headless',
        '--disable-gpu',
        '--no-margins',
        '--print-to-pdf={output_file}',
        '{input_file}'
    )

    def __init__(self,chrome_exec):
        '''
        Constructor
        chrome_exec (string) - path to chrome executable
        '''

        # check if the chrome executable path is non-empty string
        assert isinstance(chrome_exec,str) and chrome_exec != ''

        self._chrome_exe = chrome_exec

        
    def html_to_pdf(self,html_byte_string, output_file):
        '''
        Converts the given html_byte_string to PDF stored at output_file

        html_byte_string (string) - html to be rendered to PDF
        output_file (string) - file object to output PDF file  

        returns True if successful and False otherwise 
        '''

        # checks if the html string given is a valid string
        assert isinstance(html_byte_string,str)


        # create a temporary file to store the html
        with tempfile.NamedTemporaryFile(suffix='.html') as html_file:
            
            # write the contents to the file
            html_file.write(str.encode(html_byte_string))
            html_file.flush()

            temp_file_path = 'file://{0}'.format(html_file.name)

            # prepare the shell command
            print_to_pdf_command = ' '.join(self._chrome_args).format(
                chrome_exec=self._chrome_exe,
                input_file=temp_file_path,
                output_file=output_file.name
            )

            isNotWindows = not sys.platform.startswith('win32')

            try:
                # execute the shell command to generate PDF
                subprocess.run(print_to_pdf_command,shell=isNotWindows,check=True)
            except subprocess.CalledProcessError:
                return False
            
        return True






