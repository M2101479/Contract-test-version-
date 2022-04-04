import datetime

#I haven't been able to make it stop working if error happens eg invalid client name should break program but it still continues
  

def name():
  global name
  name=input('Enter your name ')
  if len(name) > 25 :
    print('Invalid Client Name')
    return('')
  return('')

def manual():
  minutes=int(input('How many minutes '))
  megabytes=int(input('Estimated amount of data in megabytes '))
  global package
  global bundle
  if minutes >= 300 and minutes < 600 :
    package = 'SMALL'
  elif minutes >= 600 and minutes < 1200  :
    package='MEDIUM'
  elif minutes >= 1200:
    package='LARGE'
  else:
    print('Enter a valid amount of minutes. There MUST be at least 300')
    return('')
  if megabytes >= 1000 and megabytes < 4000 :
    bundle='LOW'
  elif megabytes >= 4000 and megabytes < 8000 :
    bundle='MEDIUM'
  elif megabytes >= 8000 :
    bundle='HIGH'
  return ('')


def select():
  global package
  global bundle
  package=input('Enter your selected package ')
  bundle=input('Enter your data bundle ')
  return ('')

def check():
  global package
  global bundle
  y=package.upper()
  if y == 'SMALL' or y == '300' or y == 'MEDIUM' or y == '600' or y == 'LARGE' or y == '1200' :
    check=0
  else:
    check=1

  if check == 1:
    print('Select a valid package')
    return('')
  
  a=bundle.upper()
  if a == 'LOW' or a == '1 GB' or a == 'MEDIUM' or a == '4 GB' or a == 'HIGH' or a == '8 GB' or a == 'UNLIMITED' :
    check=0
  else:
    check=1

  if check == 1:
    print('Select a valid data bundle')
    return('')
  return('')
    
 

def ref_check():
  global reference
  if len(reference) != 6:
    print('Enter a valid reference number')
    return('')
  return('')
  
def ref_check2():
  ref_check=reference[0].isalpha()
  ref_check2=reference[1].isalpha()
  ref_check3=reference[2].isalpha()
  ref_check4=reference[3].isalpha()
  ref_check5=reference[4].isalpha()
  ref_check6=reference[5].isalpha()

  if ref_check is True and ref_check2 is True and ref_check3 is False and ref_check4 is False and ref_check5 is False and ref_check6 is True:
    if reference[5] == 'b' or reference[5] == 'B' or reference[5] == 'n' or reference[5] == 'N':
      check=0
    else:
      check=1
  else:
    check=1

  if check == 1:
    print('Enter a valid reference number')
    return('')
  return('')

def period():
  global periods
  periods=int(input('Enter your contracts period '))
  if periods == 1 or periods == 12 or periods == 18 or periods == 24:
     check=0
  else:
    check=1

  if check == 1:
    print('Enter a valid contract period')
    return('')
  return('')

def intl():
  global call
  intlcalls=input('Does it have international calls ')

  call=intlcalls.upper()
  if call == 'Y' or call == 'YES' or call == 'N' or call == 'NO':
    check=0
  else:
    check=1

  if check == 1:
    print('Enter a valid input for international calls')
    return('')
  return('')

def cost():
  global package
  global bundle
  global price
  price=0
  if bundle.upper() == 'LOW' or bundle == '1 GB':
    if package.upper() == 'SMALL' or package == '300':
      price=500
      package='Small  (300)'
    elif package.upper() == 'MEDIUM' or package == '600':
      price=650
      package='Medium (600)'
    elif package.upper() == 'LARGE' or package == '1200':
      price=850
      package='Large (1200)'
    data='Low (1GB)'
  if bundle.upper() == 'MEDIUM' or bundle == '4 GB':
    if package.upper() == 'SMALL' or package == '300':
      price=700
      package='Small  (300)'
    elif package.upper() == 'MEDIUM' or package == '600':
      price=850
      package='Medium (600)'
    elif package.upper() == 'LARGE' or package == '1200':
      price=1050
      package='Large (1200)'
    data='Medium (4GB)'
  if bundle.upper() == 'HIGH' or bundle == '8 GB':
    if package.upper() == 'SMALL' or package == '300':
      price=900
      package='Small  (300)'
    elif package.upper() == 'MEDIUM' or package == '600':
      price=1050
      package='Medium (600)'
    elif package.upper() == 'LARGE' or package == '1200':
      price=1250
      package='Large (1200)'
    data='High (8GB)'
  if bundle.upper() == 'UNLIMITED' :
    if package.upper() == 'SMALL' or package == '300':
      price=0
      package='Small  (300)'
    elif package.upper() == 'MEDIUM' or package == '600':
      price=0
      package='Medium (600)'
    elif package.upper() == 'LARGE' or package == '1200':
      price=2000
      package='Large (1200)'
    data='Unlimited'
  return('')


def offer():
  global discount
  global periods
  global price
  global pound
  global type
  global reference
  discount=0
  type='Normal'
  if reference[5] == 'B' or reference[5] == 'b':
    if periods >= 12:
      check=0
    else:
      check=1

    if check == 1:
      print('Business customers must at least take a 12 month contract')
      return
    discount=10
    type='Business'
  elif periods == 12 or period == 18:
    discount=5
  elif periods == 24:
    discount=10
  total=(price/100) * (100 - discount)
  pound=total/100
  if total == 0:
    total='N/A'
  return('')

def date():
  global current_day
  dt = datetime.datetime.today()
  day=str(dt.day)
  month=str(dt.month)
  year=str(dt.year)
  current_day=day + '/' + month + '/' + year
  print('')
  return('')
  
def display(): 
  global name
  global reference
  global current_day
  global package
  global bundle
  global period
  global discount
  global pound
  global type
  print('   ')
  print('Customer : ' + name )
  print('   ')
  print('Ref: ' + str(reference) + '             ' + '  ' + '             ' + 'Date:' + current_day)
  print('Package: ' + package + '             ' + '     '  + 'Data:' + bundle )
  if period == 1:
    print('Period: ' + str(periods) +  ' Month                 ' + '       '  + 'Type:' + type )
  else:
    print('Period: ' + str(periods) +  ' Months                 ' + '     '  + 'Type:' + type )
  print('   ')
  if discount == 10:
    print('Discount: ' + str(discount) + '%                 ' + '         '  + 'Intl.calls:' + call )
  else:
     print('Discount: ' + str(discount) + '%                 ' + '          '  + 'Intl.calls:' + call )
  print('   ')
  if discount != 0 :
    print('         Discounted Monthly Charge:  £' + str(pound))
  else:
    print('                   Monthly Charge:  £' + str(pound))
  with open ('I:/Downloads/summary.txt','a') as file:
    file.write(str(current_day) + '   ' + str(package) + '   ' + str(data) + '   ' + str(period) + '   ' + str(call) + '   ' + str(reference) + '   ' + str(pound) + '   ' + str(name) + '\n' )
    file.close()
  return('')
  

def summary():
  for x in range(0,4):
    file=input("Would you like the summary of current contracts or the archive ")
    # i haven't done the archive
    answers=['CURRENT','CURRENT CONTRACTS','CURRENT CONTRACT','ARCHIVE']
    if file.upper() not in answers:
      if x == 0 :
        print('Please select a valid contract. 3 attemps left')
      elif x == 1:
        print('Please select a valid contract. 2 attemps left')
      elif x == 2:
        print('Please select a valid contract. 1 attemps left')
      elif x == 3:
        return('')
    else:
      break
  if answers[0] in file.upper():
    with open ('I:/Downloads/summary.txt','r+') as file:
      print('There is currently ' + str(len(file.readlines())) + ' contracts' )
      file.close()
    with open('I:/Downloads/summary.txt') as file:
      contents=file.read()
      count=contents.count('Unlimited')
      count2=contents.count('High')
      total=count + count2
      print('There is ',total,' contracts with either high or unlimted data bundles')
      #Need to put the lines with large packages into arrays so i cann make average cost
  return('')


def month_sum():
  for x in range(0,4):
    file=input("Would you like the summary of current contracts or the archive ")
    answers=['CURRENT','CURRENT CONTRACTS','CURRENT CONTRACT','ARCHIVE']
    if file.upper() not in answers:
      if x == 0 :
        print('Please select a valid contract. 3 attemps left')
      elif x == 1:
        print('Please select a valid contract. 2 attemps left')
      elif x == 2:
        print('Please select a valid contract. 1 attemps left')
      else:
        return('')
    else:
      months=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUEST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
      for x in range(0,4):
        month=input('Select your month ')
        if month.upper() not in months:
          if x == 0:
            print('Enter a valid month. 3 attemps left ')
          elif x == 1:
            print('Enter a valid month. 2 attemps left ')
          elif x == 2:
            print('Enter a valid month. 1 attemps left ')
          else:
            return('')
        else:
          return('')

def find():
  for x in range(0,4):
    file=input("Would you like the summary of current contracts or the archive ")
    answers=['CURRENT','CURRENT CONTRACTS','CURRENT CONTRACT','ARCHIVE']
    if file.upper() not in answers:
      if x == 0 :
        print('Please select a valid contract. 3 attemps left')
      elif x == 1:
        print('Please select a valid contract. 2 attemps left')
      elif x == 2:
        print('Please select a valid contract. 1 attemps left')
      else:
        return('')
    else:
      search=input('Enter text ')
      return ('')


loop=True
while loop == True :
    print ("""
    1.Enter new Contract
    2.Display Summary of Contracts
    3.Display Summary of Contracts for Selected Month
    4.Find and display Contract
    0.Exit
    """)
    ans=input("What would you like to do? ") 
    if ans=="1": 
      package=''
      bundle=''
      print(name())
      
      choice=input('Would you like to select your bundle or manually enter your estimated minutes ')
      if choice.upper() == 'MANUALLY ENTER' or choice.upper () == 'MANUALLY' or choice.upper() == 'MANUAL':
        print(manual())
      elif choice.upper() == 'SELECT' or choice.upper () == 'CHOOSE':
        print(select())
      print(check())
      reference=input('Enter your reference number ')
      print(ref_check())
      print(ref_check2())
      print(period())
      print(intl())
      print(cost())
      print(offer())
      print(date())
      print(display())
      print(discount)
      print(package,bundle)
    elif ans=="2":
      print(summary()) 
    elif ans=="3":
      print(month_sum())
    elif ans=="4":
      print(find()) 
    elif ans=='0':
      loop=False
    elif ans !="":
      print("\n Not Valid Choice Try again") 
