numb<-floor(runif(1, min=0, max=101))
print(numb)


guess<-1
while (guess<=3)
{
mynumb <- readline(prompt="Enter your number: ")

if (numb==mynumb) {
  print("yes this is right")
  guess<-guess+1
} else if (numb<mynumb) {
  print("The number is smaller")
  guess<-guess+1
} else if (numb>mynumb){
  print("The number is bigger")
  guess<-guess+1
}
}
