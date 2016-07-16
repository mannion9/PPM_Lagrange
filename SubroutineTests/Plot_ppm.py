import matplotlib.pyplot as plt
show  = 0 # Set to 0 to see whole solution and 1 to see uL and uR and interpolation

domain = open('Output/domain.txt')     # Cell centers   (0,Nx-1)   array
cell   = open('Output/cells.txt')      # Cell edges     (0,Nx)     array
a      = open('Output/a.txt')          # PPM solution  Nt*(0,Nx-1) arrays
a_true = open('Output/true.txt')       # True solution Nt*(0,Nx-1) arrays 
#a_first= open('Output/a_first_0.txt')  # First order   Nt*(0,Nx-1) arrays
al     = open('Output/uL.txt')         # aL            Nt*(0,Nx-1) arrays
ar     = open('Output/uR.txt')         # aR            Nt*(0,Nx-1) arrays
a12    = open('Output/u12.txt')        # a12           Nt*(0,Nx-1) arrays

#files  = [domain,cell,a,a_true,a_first,al,ar,a12]
files  = [domain,cell,a,a_true,al,ar,a12]


# Read in
file_list =[]
content=[]
for file_ in files:
  file_list.append(file_.read().splitlines())
for data in file_list:
  events = []
  for line in data:
    row= []
    line = line.split(' ')
    for i in line:
      if i != '':
        row.append(float(i))
    events.append(row)
  content.append(events)

domain = content[0][0]
cells  = content[1][0]
a      = [content[2][i] for i in range(len(content[2]))]
a_true = [content[3][i] for i in range(len(content[2]))]
#a_first= [content[4][i] for i in range(len(content[2]))]
al     = [content[4][i] for i in range(len(content[2]))]
ar     = [content[5][i] for i in range(len(content[2]))]
a12    = [content[6][i] for i in range(len(content[2]))]
dx     = domain[1]-domain[0]

# domain = content[0][0]
# cells  = content[1][0]
# a      = [content[2][i] for i in range(len(content[2]))]
# a_true = [content[3][i] for i in range(len(content[2]))]
# a_first= [content[4][i] for i in range(len(content[2]))]
# al     = [content[5][i] for i in range(len(content[2]))]
# ar     = [content[6][i] for i in range(len(content[2]))]
# a12    = [content[7][i] for i in range(len(content[2]))]
# dx     = domain[1]-domain[0]

if show == 0:
    #for i in range(0,5):
    for i in range(0,len(a)-1,10):
        approx = plt.scatter(domain,a[i],marker='*')
        true,  = plt.plot(domain,a_true[i])
        plt.xlabel('x'),plt.ylabel('a')
        plt.title('Itteration %i ' %i)
        plt.legend((true,approx),('True','PPM'))
        plt.show()

if show == 1:
  for i in [0]:
      approx = plt.bar(domain,a[i],width=dx,color='white',alpha=.5,align='center')
      uL     = plt.scatter(cells,al[i],c='g')
      uR     = plt.scatter(cells,ar[i],c='r')
      A12,   = plt.plot(cells,a12[i],c='black',linewidth=2)
      plt.xlabel('x'),plt.ylabel('a')
      plt.legend((approx,uL,uR,A12),('PPM','aL','aR','Interpolation'))
      plt.title('Itteration %i ' %i)
      plt.xlabel('x'),plt.ylabel('a')
      plt.show()
