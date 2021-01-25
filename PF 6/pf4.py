'''4. Assume variables first, last, street, number, city, state, zip code have already been assigned
in a function mailaddress(). When you pass all the parameters it generates a mailing label:
Syed Faisal Ali
Asst. Prof.
Department of Computer Science
Usman Institute of Technology
Gulshan e Iqbal, 75300
Karachi.
'''

def mailaddress(ft, lt, srt, cty, st, z_cd):
    print('{} {} \n{}\n{}, {}.\n{}.'.format(ft, lt, srt, cty, st, z_cd))
mailaddress('Muhammad', 'Nasir', 'Usman Institute of Technology', 'Gulshan e Iqbal', '75300', 'Karachi')
    

