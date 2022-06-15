dict = {
  'M' : 1000,
  'CM' : 900,
  'D' : 500,
  'CD' : 400,
  'C' : 100,
  'XC' : 90,
  'L' : 50,
  'XL': 40,
  'X' : 10,
  'IX' : 9,
  'V' : 5,
  'IV' : 4,
  'I' : 1,
}

def convert_to_roman(num):
    res = ""

    for i in dict:
        while num >= dict[i]:
            num -= dict[i]
            res += i
    return res

def main():
    res = convert_to_roman(1024)
    
    print(f"1024 is: {res}")

if __name__ == '__main__':
    main()
