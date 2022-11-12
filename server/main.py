import glob
import shutil
import os
from zipfile import ZipFile
while True:
      source_path="..\source\*"
      destination_path="..\destination"
      postfix=[1,2,3]
      source_obj= glob.glob(source_path)
      li_txt=[]
      li_py=[]
      for i in source_obj:
            i_split=i.split('\\')[-1]
            pre,post =i_split.split(".")
            if post =="txt":
                  li_txt.append(i)
            if post =="py":
                  li_py.append(i)

      for txt in li_txt:
            
            shutil.copy(txt,'.')

            object_name=txt.split('\\')[-1]
            with open(object_name,"r") as file:
                  lines =file.readlines()
            file.close()
            object_pre_post=object_name.split(".")
            
            prefix =object_pre_post[0]
            postfix_2=object_pre_post[1]
            os.remove(f"../server/{object_name}")
            shutil.make_archive(prefix, "zip")
            zip_name=f"{prefix}.zip"
            zip_obj = ZipFile(zip_name, 'w')
            for item in postfix:
                  file_name =prefix+"_"+str(item)+"."+postfix_2
                  with open(file_name,"w")as file:
                        for i in range(item*10):
                              line= file.write(lines[i])
                  file.close()
                  zip_obj.write(file_name)
                  os.remove(file_name)

            zip_obj.close()

            shutil.copy(zip_name,f"{destination_path}\{zip_name}") 
            os.remove(f"../server/{zip_name}")    

            with ZipFile(f"{destination_path}\{zip_name}", 'r') as zObject:
      
      
                  zObject.extractall(path=f"{destination_path}")

            zObject.close()
            os.remove(f"../destination/{zip_name}")
            os.remove(f"../source/{object_name}")

      for py in li_py:
            os.system(f'python {py}')
           




      





