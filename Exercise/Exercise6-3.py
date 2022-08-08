favor_langs = {
    'zhang':'python',
    'li':'java',
    'wang':'go',
    'lin':'php',
}
suverys = ['li','zhang','liu','wang']

for suvery in suverys:
    if suvery in favor_langs.keys():
        print ('Thanks for coodinate our suvery, ' + suvery)
    else:
        print ('Would u like join to this suvery, '+ suvery +'?')
