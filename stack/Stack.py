#################################################################################
#                                        STACK                                  #
#                                                                               #        
#              Basic data Type is Python Array to implement Stack Operations    #
#                                                                               #       
#################################################################################


#############################################
#            function to implemented        #   
#  1 - Pop                                  #
#  2 - Push                                 #   
#  3 - Peek                                 #       
#  4 - Size                                 #           
#  5 - isEmpty                              #                       
#############################################


class  Stack(object):

    def __init__(self):
        self.Stack = []
    
    def isEmpty(self):
        return  True if len(self.Stack) == 0 else False

    '''@symbol'''
    def push(self,data):
        self.Stack.append(data)
    
    def pop(self):
        if self.isEmpty() :
           print('stack is empty')
        else :
            data  = self.Stack[-1]
            del self.Stack[-1]
            return data
        
    def peek(self):
        if len(self.Stack) == 0:
            print('stack is empty')
        else :
            return self.Stack[-1]
    
    def size(self):
        return len(self.Stack)

    pass


def main():

    stk = Stack()
    stk.push('C#')
    stk.push('Python')
    stk.push('Java')
    print(stk.peek())
    stk.push('12')
    
    print(stk.pop())


    pass

if __name__ == '__main__':
    main()
    pass 

    