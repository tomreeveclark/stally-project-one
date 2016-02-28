import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stally_project.settings')

import django
django.setup()

from stally.models import Market, Stall


def populate():
    paddington_market = add_market('Paddington Markets','Paddington Town Hall',-33.885019,151.226055)

    add_stall(market=paddington_market,
        name="Tom's Stall"
        )    
    
    add_stall(market=paddington_market,
        name="Charlotte's Stall"
        )
    
    add_stall(market=paddington_market,
        name="Merrie's Stall"
        )
    
    eastwood_market = add_market('Eastwood Markets','Eastwood Main Oval',-33.788815,151.081426)

    add_stall(market=eastwood_market,
        name="Jack's Stall"
        )
    
    add_stall(market=eastwood_market,
        name="Kate's Stall"
        )
    
    add_stall(market=eastwood_market,
        name="Paul's Stall"
        )
    
    glebe_market = add_market('Glebe Markets','Sydney University',-33.887670,151.186112)

    add_stall(market=glebe_market,
        name="Andrew's Stall"
        )
    
    bondi_market = add_market('Bondi Markets','Bondi Beach',-33.890875,151.276391)

    add_stall(market=bondi_market,
        name="Bronwyn's Stall"
        )
    
    add_stall(market=bondi_market,
        name="Rachael's Stall"
        )
    
    add_stall(market=bondi_market,
        name="Emma's Stall"
        )
       

    # Print out what we have added to the user.
    for m in Market.objects.all():
        for s in Stall.objects.filter(market=m):
            print("- {0} - {1}".format(str(m), str(s)))

def add_market(name, location,lat,lng):
    m = Market.objects.get_or_create(name=name)[0]
    m.location=location
    m.lat=lat
    m.lng=lng
    m.save()
    return m

def add_stall(market,name):
    s = Stall.objects.get_or_create(name=name, market=market)[0]
    return s

# Start execution here!
if __name__ == '__main__':
    print("Starting Stally population script...")
    populate()