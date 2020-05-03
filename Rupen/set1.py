from csv import DictReader, DictWriter, writer

s={'Ravin'}
with open('data1.csv','r') as rf:
    csv_reader=DictReader(rf)
    for name in csv_reader:
        s.add(name['name'])

with open("aaa.txt",'r') as rf1:
    lines=rf1.readlines()
    for line in lines:
        s.add(line)

# print(s)
with open("set4.csv",'a',newline="") as wf:
    csv_writer=DictWriter(wf,fieldnames=['name'])
    csv_writer.writeheader()
    for name in s:
        csv_writer.writerow({
            'name':f'{name}'
        })
    

