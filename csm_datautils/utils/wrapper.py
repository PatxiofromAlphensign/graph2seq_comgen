import argparse
import os
import numpy as np

class getPath:
    def __init__(self, path):
        """
        constructs iterable over all the paths across the range of files in `path` 
        """ 
        self.all_lines = []
        for fi in os.listdir(path):
            with open(os.path.join(path,fi), 'r') as r:
                self.all_lines.append(r.readlines())

    def __getitem__(self, key):
        return self.all_lines[key]
            
    
    def split_cat(self):
        self.sc = []
        sc = {}
        for k in self.all_lines:
            sc = {x : i for i,x in enumerate(k[0].split('/'))}
            self.sc.append(sc)
        return self.sc            
    def list_byidx(self, query)->iter:
        """
            query by index 
        """
        itr = []
        for batch in self.all_lines:
            for i,k in enumerate(batch):

                label_idx = self.split_cat()[0]['cdx-00000.gz\n']
                if query in k.split('/')[-1]:
                    itr.append(batch[i])
        return itr

    def list_bydate(self, query):
        """
            query by bydate 
        """

        itr = []
        
        for c,batch in enumerate(self.all_lines):
            for i,k in enumerate(batch):
                label_idx = self.split_cat()[0]['CC-MAIN-2020-24']

                if query in k.split('/')[label_idx]:
                    itr.append(batch[i])
        return itr

    
    def map2dict(self):
        self.mapped = {}
        for b in self.all_lines:
            for k in b:
                self.mapped[k.split('/')[-1]] = k.split('/')[:-1]

        return self.mapped

def querywithmaxrange(path,query, max_range):
    idx = path.list_byidx(query)[:max_range] 
    return idx

def namesbyrange(path, rng):    
    "returns data per idx"
    idxs = path.list_byidx('0%d' % rng) 
    w_date = path.list_bydate('2020') # for just 2020 demo
    return len(idxs)
    #return path.map2dict()

def autobatched_dataset(id_list):
    pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir',help='dir' ,default='data', type=str)
    args = parser.parse_args()

    path = getPath(args.dir)
    print((namesbyrange(path, 111)))

