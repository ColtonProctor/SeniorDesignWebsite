import csv, sys, os
import pandas as pd

project_dir = "/Users/colton_proctor/Desktop/seniorProject/mySite"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE']='mySite'

import django
django.setup()

from main.models import Property

data = pd.read_csv('/Users/colton_proctor/Desktop/seniorProject/mySite/db.csv') #,delimiter="|")
#data = csv.reader(open('/Users/cohen/my-python-project/venv/ofac/ofac_project/ofac_sdn/sdn2.csv'), dialect='excel-tab')
for index, row in data.iterrows():
        property = Property()
        property.state = row[0]
        property.recorded = row[1]
        property.date = row[2]
        property.grantor = row[3]
        property.address = row[4]
        property.city = row[5]
        property.grantee = row[6]
        property.price = row[7]
        property.propType = row[8]
        property.built = row[9]
        property.acreage = row[10]
        property.impsq = row[11]
        property.units = row[12]
        property.landsq = row[13]
        property.sfimp = row[14]
        property.unitimp = row[15]
        property.sfland = row[16]
        property.garage = row[17]
        property.caprate = row[18]
        property.noi = row[19]
        property.exp = row[20]
        property.egi = row[21]
        property.occup = row[22]
        property.corner = row[23]
        property.regshape = row[24]
        property.utilities = row[25]
        property.location = row[26]
        property.quality = row[27]
        property.condition = row[28]
        property.description = row[29]
        property.comments = row[30]
        property.save()