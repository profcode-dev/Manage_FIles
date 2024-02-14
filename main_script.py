import os
from time import sleep 
import shutil

print("######### Welcome to my program ########\n -- Just give me the location and step back, to do my work..👌👌😉")
while True: 
    try:
        action_location = input("Please,Enter the location (to manage your files): ")
    except KeyboardInterrupt: 
        exit()
    except ValueError:
        print("Enter correct value")
        
    sleep(0.5)
    sort = os.listdir(action_location)

    for f in sort:   # 'f' is a list for files 
        try: 
            # move photos
            if f.endswith(('png','jpg','ico','jpeg','JPG','JPEG','GIF','PNG','webp')):
                location = os.path.join(action_location, 'Images')
                os.makedirs(location, exist_ok=True)
                # make source and destination 
                source = os.path.join(action_location, f) 
                shutil.move(source , location)
                
                sleep(0.5)
                print(f"{f} Moved..")
            # move videos
            elif f.endswith(('mp4','mkv','mov','avi','wmv','webm','flv','f4v','avchd','m4v')):
                location = os.path.join(action_location, 'Videos')
                os.makedirs(location, exist_ok=True)
                
                source = os.path.join(action_location, f)
                shutil.move(source , location)
                
                sleep(0.5)
                print(f"{f} Moved..")
            # move audios and voices 
            elif f.endswith(('mp3','pcm','PCM','wav','WAV','aiff','AIFF','acc','ACC')):
                location = os.path.join(action_location, 'Audios')
                os.makedirs(location, exist_ok=True)
                
                source = os.path.join(action_location, f)
                shutil.move(source , location)
                
                sleep(0.5)
                print(f"{f} Moved..")
            # move programs , excecute files
            elif f.endswith(('exe')):
                location = os.path.join(action_location, 'Programs')
                os.makedirs(location, exist_ok=True)
                
                source = os.path.join(action_location, f)
                shutil.move(source , location)
                
                sleep(0.5)
                print(f"{f} Moved..")
            # move document files
            elif f.endswith(('pdf','txt','docx','html','xlsx','py','ipynb','pptx','css','cpp')):
                if f.endswith(('pdf')):
                    location = os.path.join(f'{action_location}\Documents', 'pdf_files')
                    os.makedirs(location, exist_ok=True)
                    
                    source = os.path.join(action_location, f)
                    shutil.move(source , location)
                else:
                    location = os.path.join(action_location, 'Documents')
                    os.makedirs(location, exist_ok=True)
                    
                    source = os.path.join(action_location, f)
                    shutil.move(source , location)
                
                sleep(0.5)
                print(f"{f} Moved..")
            # zip folders 
            elif f.endswith(('rar','zip')):
                location = os.path.join(action_location, 'zip_folders')
                os.makedirs(location, exist_ok=True)
                
                source = os.path.join(action_location, f)
                shutil.move(source , location)
                
                sleep(0.5)
                print(f"{f} Moved..")
            else:
                print(f'{f}Failed To move..')
        except:
            print("There are an error you can restart the program")

    print("Process Successfully DONE")
    
    print("----------------------------------------------------------------")
    print("Developed By Eng-Hossam Elsawy       V.2.1")
    print("==================================================================================================")
    question = input("\n>> Do you want to continue (y/n): ")
    if question != 'y': 
        break






