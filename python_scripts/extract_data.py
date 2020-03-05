# create a summary for the data base
# output format: markdown table
import json
import yaml

import os

os.system('cp table_header.md readme.md')

def table_entry_dump(data_list):
    #return markdown table entry for a new line
    
    pass

    
def check_filename(filename, path):
    # check first
    if filename == '../../README.md' :
        return ''
    return load_data(filename, path)

def get_first_link(line):
    #return the first link in a markdown line
    a=line.split('(')
    b=a[1].split(')')
    link = b[0]
    return link

def load_data(filename,path):
    #return a json object defined by sample.yml
    article={}
    article['filename']=filename[len(path):]
    article['title']=filename.split('-')[-1][:-3]
    print(filename)
    title = filename
    pics='no pics'
    date='no date'
    link='no link'
    with open(filename,'r') as f:
        #for line in f.readlines():
        for line in f:            
            if line =='\n':
                pass
            elif line[0:9] == '已获得作者转载授权':
                article['authorization'] = 'yes'
            elif line[0:2] == '来源':
                try:
                    sources= line[2:].split('的')
                    if len(sources) > 1:
                        article['author']=sources[0].split(']')[0][1:]
                        article['author_url']=sources[0].split('(')[1][:-1]
                        article['source']=sources[1].split(']')[0][1:]
                        article['source_url']=sources[1].split('(')[1][:-1]
                    else:
                        article['source_url'] = sources
                        
                    link = get_first_link(line)
                    link = '[link]('+link+')'
                except:
                    link = 'no link'
                #print(line)
            elif line[0:2] == '20':
                date = line[0:-1]
                article['long_date']=line[:-1]
                #finish reading file header
                break
                #print(line)
            elif line[0:2] == '![':
                pics=get_first_link(line)
                pics = '../../'+pics
                #pics = '[pics]('+ pics +')'
                pics = '<a href="'+ pics +'">pics</a>'

        content=''
        pics_list=[]
        for line in f:#.readlines():
            if line[0:2] == '![':
               pics_list.append({
                   'name': line.split('(')[1][:-1],
                   'url': line.split('(')[1][:-1]
               })
            else:
                content += line
    article['content']= content
    article['pics']=pics_list
                
            #if ( line[0:3]
    #print([date,title,link,filename,pics])
    #filename = '[file]('+filename+')'
    filename = '<a href="'+filename+'">file</a>'
    title='<a>'+title+'</a>'
    raw=[date,title,link,filename,pics]
    #for item in raw:
        #item = item.replace(' ','%20')
        #item = item.replace('\n','')
    table_raw = ' | '.join(raw)
    #table_raw = table_raw.replace(' ','%20')
    #table_raw.replace('\n','')
    table_raw = ('| '+ table_raw + ' |\n')
    #return [date,title,link,filename,pics]
    #return (json.dumps(article, indent=2))
    return article
    #return table_raw

import glob

'''
with open('data/articles.json', 'w') as f:

    path='../archives/'
    f.write('[\n')
    #for filename in os.listdir(path):
        #table_raw = check_filename(path+filename)
    for filename in glob.glob(path+'*.md'):   
        table_raw = check_filename(filename,path)
        #print(table_raw)
        #break
        f.write(table_raw+',\n')
    f.write(']')
'''

path='../archives/'
write_path='../docs/_data/articles/'
write_path='../docs/_data/yaml/'

for filename in glob.glob(path+'*.md'):   
    table_raw = check_filename(filename,path)
        #print(table_raw)
        #break
    with open(write_path+filename[len(path):-3]+'.yml','w') as f:
        f.write(yaml.dump(table_raw))
    

