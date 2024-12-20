from django.shortcuts import render

# Create your views here.
def main(request): # step 10
    context ={
        'name':'Kendrick Lamar',
        'title':'DAMN', 
        'song1':'BLOOD.',
        'song111':'DNA.',
        'song2':'YAH.',
        'song3':'ELEMENT.',
        'song4':'FEEL.',
        'song5':'LOYALTY.FEAT.RIHANNA',
        'song6':'PRIDE.',
        'song7':'HUMBLE.',
        'song8':'LUST',
        'song9':'LOVE.FEAT.ZACARI.',
        'song10':'XXX.FEAT.U2',
        'song11':'FEAR',
        'song12':'GOD',
        'song13':'DUCKWORH',
        'test':"The Compton rapper's fourth studio release explored themes of inequality, religion, and a person's inner struggle with good and evil."
    }
    return render(request, 'index.html',context=context)