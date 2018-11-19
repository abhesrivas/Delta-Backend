import numpy as np
import pandas as pd

def cat_similarity(input_laptop,laptops,test_indices,cat_cols):
        
    similarity_score = []
    
    for index, row in laptops.iterrows():
        if index not in test_indices:
            common_total = 0
            for col in cat_cols:
                text_1 = input_laptop[col]
                text_2 = row[col]
                document_1_words = text_1.split()
                document_2_words = text_2.split()
                common = len(set(document_1_words).intersection( set(document_2_words)))
                common_total+=common
            similarity_score.append(common_total/25)
    return similarity_score
        
def num_similarity(input_laptop,laptops,test_indices,num_cols):

    similarity_score = []
    
    for index, row in laptops.iterrows():
        if index not in test_indices:
            common_total = 0
            for col in num_cols:
                num_1 = input_laptop[col]
                num_2 = row[col]
                common = 1/((np.abs(num_1 - num_2)/np.mean(laptops[col]))+1)
                common_total+=common
            similarity_score.append(common_total)
    return similarity_score

def get_recommendations(test_indices):
        
    laptops = pd.read_csv('/home/ubuntu/Box/Delta/Miscelleneous/Datasets/laptops_with_photo_url.csv')
    
    laptops.drop(['Unnamed: 0','photo_url'],axis=1,inplace=True)
    
    # string to int
    laptops['Ram'].replace(regex=True,inplace=True,to_replace=r'GB',value=r'')
    laptops['Ram'] = laptops['Ram'].apply(int)
    
    laptops['Weight'].replace(regex=True,inplace=True,to_replace=r'kg',value=r'')
    laptops['Weight'] = laptops['Weight'].apply(float)
    
    cat_cols = ['Company','Product','TypeName','ScreenResolution','Cpu','Memory','Gpu','OpSys']
    num_cols = ['Inches','Ram','Weight','Price_euros']
        
    indices_list = []
    
    for i in range(len(test_indices)):
        test_index = test_indices[i]
        test_laptop = laptops.iloc[test_index]
                
        cat_scores = np.array(cat_similarity(test_laptop,laptops,test_indices,cat_cols))
        num_scores = np.array(num_similarity(test_laptop,laptops,test_indices,num_cols))
        
        total_scores = cat_scores + 0.01*num_scores
        total_indices = list((-total_scores).argsort()[:10])
#        print(total_indices)
        
        indices_list.append(total_indices)

#    print('Indices List: ', indices_list)
        
    for i in range(len(indices_list)):
        indices_list[i] = indices_list[i][:10]
    
#    print('Indices List: ', indices_list)

    final_rec = []
    for i in range(len(indices_list)):
        final_rec+=indices_list[i]
    
    imp = [0,1,10,11,20,21,30,31,40,41]
    final_rec = [final_rec[x] for x in imp]
    
#    print('Final_Rec: ', final_rec)
    
    indi_dicts = []
    for i in range(len(final_rec)):
        indi_dicts.append({'Company':laptops['Company'][final_rec[i]],
                               'Product':laptops['Product'][final_rec[i]],
                               'Price_euros':laptops['Price_euros'][final_rec[i]]})
        
    final_dict = {'count':len(indi_dicts), 'results':indi_dicts}
    
    return final_dict
