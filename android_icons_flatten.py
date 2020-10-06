import sys, os, re, codecs, shutil
import zipfile


p  = 'd:/GitHub/material-design-icons/android/'
o  = 'd:/material-design-icons/'
oz = 'd:/material-design-icons-zip/'


dens = [
  'drawable-hdpi',
  'drawable-mdpi',
  'drawable-xhdpi',
  'drawable-xxhdpi',
  'drawable-xxxhdpi',
]


def get_filenames(root_dir):
  for root, dirs, files in os.walk(root_dir):
    return files
    
def get_dirnames(root_dir):
  for root, dirs, files in os.walk(root_dir):
    return dirs

def get_dirpaths(root_dir):
  res_list = []
  for root, dirs, files in os.walk(root_dir):
    for dirr in dirs:
      res_list.append(os.path.normpath(os.path.join(root, dirr)))
    return res_list
    

def run():
  for d in get_dirpaths(p):
    for i in get_dirnames(d):
      print(i)
      themes_d = get_dirnames(d + '/' + i)
      for td in themes_d:
        print('  - ' + td)
        t_p = d + '/' + i + '/' + td + '/'
        ot_p = o + i + '/' + td + '/'
        
        ic_names = get_filenames(t_p + 'black/res/drawable-hdpi/')
        for ic_f in ic_names:
          ic_n = os.path.splitext(ic_f)[0]
          for dens_f in dens:
            os.makedirs(ot_p + ic_n + '/res/' + dens_f, exist_ok=True)
        
        for ic_f in ic_names:
          ic_n = os.path.splitext(ic_f)[0]
          shutil.copytree(t_p + 'black/res/drawable', ot_p + ic_n + '/res/drawable', dirs_exist_ok=True)
          
          for dens_f in dens:
            shutil.copy(t_p + 'black/res/' + dens_f + '/' + ic_f, ot_p + ic_n + '/res/' + dens_f + '/' + ic_f)

def run_zip():
  icn = get_dirnames(o)
  
  for i in icn:
    print(i)
    themes_d = get_dirnames(o + i)
    for td in themes_d:
      print('  - ' + td)
      ot_p = o + i + '/' + td + '/'
      oz_p = oz + i + '/' + td + '/'
      
      os.makedirs(oz_p)
      
      sizes_p = get_dirpaths(ot_p)
      for sp in sizes_p:
        out_name = os.path.basename(sp)
        os.chdir(os.path.dirname(sp))
        shutil.make_archive(oz_p + out_name, "zip", out_name)


# ---
run()
# run_zip()
