import zipfile
import os

zipfile_name = 'query'                                                                       # Chinh ten file zip
zipfile_path = os.path.join('E:/private', zipfile_name +'.zip')    # Chinh duong dan den file zip
dest_path = 'view-res/queries'                                                                      # Chinh duong dan den noi mong muon

def extract_zipfile():
    if not os.path.exists(os.path.join(dest_path, zipfile_name)): # include this to not overwrite
        with zipfile.ZipFile(zipfile_path, 'r') as zf:
            zf.extractall(os.path.join(dest_path, zipfile_name))
        print('Create query dir!')
    else:    
        print('Query dir alr exist!')
    pass    

def create_csv():
    csv_dirpath = os.path.join(dest_path, zipfile_name + '/submisson_data')
    txt_files= os.listdir(os.path.join(dest_path, zipfile_name))   
    ok = False 
    if not os.path.exists(csv_dirpath): # include this to not overwrite
        os.makedirs(csv_dirpath)                                               # Tao thu muc ten = zipfile_name chua file csv
        ok = True  
        print('Create empty csv dir!')      
    elif len(os.listdir(csv_dirpath)) == 0:
        ok = True
        print('Empty csv dir alr exist!')           

    if ok:   
        for txt_file in txt_files:                              # 30 -> 33: Tao file csv ten = queries  
            csv_file = txt_file.split('.')[0] + '.csv'
            with open(os.path.join(csv_dirpath, csv_file), 'w'):
                pass
        print(f'Create csv files in {csv_dirpath}')
    else:        
        print('cvs dir not empty!')         
    pass        

extract_zipfile()
create_csv()   