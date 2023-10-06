arr = []
i = 0
j = 0
while True:
    try:
        n = int(input("Введите количество строк n= "))
        m = int(input("Введите количество столбцов m= "))
        break
    except ValueError:
        print("Введены некорректные значения!")
while i < n:
    st=[]
    j=0
    if i % 2 == 0:
       while j<m:
           if j%2==0:
               st.insert(j,"%")
           else:
               st.insert(j+1, "#")
           j+=1
    else:
       while j<m:
           if j%2==0:
               st.insert(j,"#")
           else:
               st.insert(j+1, "%")
           j+=1
    arr.append(st)
    i+=1
if n>0 and m>0:
    arr[0][0]="."
for i in arr:
    print(i)


