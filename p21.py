# First project using Python

# FILE SAPARATOR APPLICATION



import os,shutil

# NOTE:    you can write every singlr extensions inside tuple


dict_extensions={
            'audio_extensions'          :   ('.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl'),
            'compressed_file_extensions':   ('.7z','.arj','.deb','.pkg','.rar','.rpm','.tar.gz','.z','.zip'),
            'disc_and_media_extensions' :   ('.bin','.dmg','.iso','.toast','.vcd'),
            'database_file_extensions'  :   ('.csv','.dat','.db','.dbf','.log','.mdb','.sav','.sql','.tar','.xml'),
            'email_extensions'          :   ('.email','.eml','.emlx','.msg','.oft','.ost','.pst','.vcf'),
            'executable_extensions'     :   ('.apk','.bat','.bin','.cgi','.pl','.com','.exe','.gadget','.jar','.msi','.py','.wsf'),
            'font_file_extensions'      :   ('.fnt','.fon','.otf','.ttf'),
            'image_extensions'          :   ('.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg','.tif','.tiff'),
            'web_extensions'            :   ('.asp','.aspx','.cer','.cfm','.cgi','.pl','.css','.htm','.html','.js','.jsp','.part','.php','.py','.rss','.xhtml'),
            'presentation_extensions'   :   ('.key','.odp','.pps','.ppt','.pptx'),
            'programming_extensions'    :   ('.c','.class','.cpp','.cs','.h','.java','.pl','.sh','.swift','.vb'),
            'spreadsheet_extensions'    :   ('.ods','.xls','.xlsm','.xlsx'),
            'system_realated_extensions':   ('.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.icns','.ico','.ini','.lnk','.msi','.sys','.tmp'),
            'video_extensions'          :   ('.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv'),
            'file_extensions'           :   ('.doc','.docx','.odt','.pdf','.rtf','.tex','.txt','.wpd'),
}

folderpath=input("Please Enter Path:\n")

def file_finder(folder_path,file_extension):   
    # files=[]
    # for file in os.listdir(folder_path):
    #     for extension in file_extension:   
    #         if file.endswith(extension):   
    #             files.append(file)
    # return files
    return [file for file in os.listdir(folder_path) for extension in file_extension if file.endswith(extension)]





# print(file_finder(folderpath,file_extensions))           #o/p: ['r.pdf']
# s=[]
# s=os.listdir(folderpath)

for extension_type, extension_tuple in dict_extensions.items():
    folder_name=extension_type.split('_')[0].title()+" Files"
    folder_path=os.path.join(folderpath,folder_name)
    # if folder_name not in s:
    #     os.mkdir(folder_path)
    for files in file_finder(folderpath,extension_tuple):
        if os.path.exists(folder_path):
            pass
        elif files==[]:
            pass
        else:
            os.mkdir(folder_path)
        item_old_path=os.path.join(folderpath,files)
        item_new_path=os.path.join(folder_path,files)
        shutil.move(item_old_path,item_new_path) 



    # print("calling filefinder...\n")
    # print(file_finder(folderpath,extension_type))



