patient = {
    'first_name': 'John',
    'last_name': 'Mutua',
    'date_of_birth': '2000-01-25',
    'mobile': '0724123456'    
}
    
def addStar(val):
    str_len = len(val)
    start = val[:2]
    no_of_stars = "*"*(str_len-2)
    masked = start+no_of_stars
    return masked

def mask_date(date):
    date_array = date.split('-')
    print(date_array)
    date_masked_arr = []
    for i in date_array:
        dd = ""
        if len(i)==2:
            dd = i[0]+"*"
        else:
            dd = i[:2]+"**"
        date_masked_arr.append(dd)
    datemasked = "-".join(date_masked_arr)
    print(datemasked)
    return datemasked
    

def mask_values(val_obj):
    print(val_obj)
    for item in val_obj:
        print(item)
        if item.find('date') != -1:
            date_msk = mask_date(val_obj[item])
            patient[item] = date_msk
        else:
            item_key = val_obj[item]
            patient[item] = addStar(item_key)
    print(patient)
    return patient
        

    
    
if __name__ == '__main__':
    mask_values(patient)