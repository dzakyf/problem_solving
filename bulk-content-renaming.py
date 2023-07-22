import os 


def append(): 
    cwd = os.getcwd()
    os.chdir(cwd)
    append_this = input("Input words to be appended: ")

    for _, current_name in enumerate(os.listdir(cwd)):
        #get filename only 
        filename = os.path.splitext(current_name)[0]
        extension = os.path.splitext(current_name)[1]

        #modify new filename 
        result = filename + append_this + extension

        #rename 
        os.rename(current_name, result)
        
    print("===== Success ! =====")



def switcher(i):
    switcher = {
        "1": append,
        # "2": replace,
    }
    
    func = switcher.get(i, lambda: "Invalid")
    return func()


def main():
    s = f"""
    {'-' * 40}
    # 1. append words into filename
    {'-' * 40}
    """
    print(s)

    s_input = input("Enter your option: ")
    switcher(s_input)

  

if __name__ == '__main__':
    main()
