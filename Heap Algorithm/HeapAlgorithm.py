def heapify(array, size, i):
    max = i  # Initialize largest as root
    left = 2 * i + 1  # left subtree  = 2*i + 1
    right = 2 * i + 2  # right subtree= 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if left < size and array[i] < array[left]:
        max = left

        # See if right child of root exists and is
    # greater than root
    if right < size and array[max] < array[right]:
        max = right

        # Change root, if needed
    if max != i:
        array[i], array[max] = array[max], array[i]  # swap

        # Heapify the root.
        heapify( array, size, max )

    # The main function to sort an array of given size


def heapSort(array):
    size = len( array )

    # Build a maxheap.
    # Since last parent will be at ((size//2)-1) we can start at that location.
    for i in range( size // 2 - 1, -1, -1 ):
        heapify( array, size, i )

        # One by one extract elements
    for i in range( size - 1, 0, -1 ):
        array[i], array[0] = array[0], array[i]  # swap
        heapify( array, i, 0 )




# sorting function above ends here, below there is main part user input
array=list()
size=int(input("Ödemek istediğiniz borç sayısınız giriniz: ")) #kullanıcı borç sayısının alınması
print("Sırasıyla Borçlarınızı giriniz :")  #borçların kullanıcıdan alınması
for i in range(int(size)):
   k=int(input(" "))
   array.append(k)
   heapSort( array )
print( "Borçlarınız sırasıyla :", end=" " )  #borçların kullanıcıya sıralanması
for i in range(size):
        print( array[i], end=" " )
print("\n")
minNumber = array[0]
maxNumber = array[0]
toplam= 0
ortalama = 0

for i in range(int(size)):
    if minNumber > array[i]:
        minNumber = array[i]  #this find the minimum dept and the maximum dept
    if maxNumber < array[i]:
        maxNumber = array[i]
print("En yüksek fiyatlı ödemeniz gereken borcunuz : {0} TL ".format(maxNumber))  #borç detaylarının kullanıcıya bildirilmesi
print("En düşük fiyatlı ödemeniz gereken borcunuz  : {0} TL".format(minNumber))

for i in range(0,len(array)):
     toplam+= array[i]
ortalama=toplam/len(array)

print('Ödemeniz Gereken Toplam Borcunuz : {} TL '.format(toplam))
print('Bu aylık Ortalama Borç Tutarınız : {} TL '.format(ortalama))












