class Solution:
    def simplifyPath(self, path: str) -> str:
        # this is a bit of a stack problem 
        # with string manipulation
        
        path = path.split('/')

        # so we need to only be a 
        # bit wary of a few 
        # "special" cases
        stack = []
        for file in path:
            if file == '..':
                # this is previous directory
                if stack:
                    stack.pop()
            elif not file or file == '.':
                # this is current directory
                # isntace of not file because we 
                # did splitting based on "/"
                continue
            else:
                stack.append(file)
        return '/'+'/'.join(stack)