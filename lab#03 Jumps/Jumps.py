import sys
import dis

class UnknownLabel(RuntimeError):
    pass

global label
class _label:
    def __getattr__(self, n): # Just make it accept any attribute
        return 42
    
label = _label()

global _labels
_labels = {}
class _goto:
    def __getattr__(self, name):
        global _labels
        
        frame = sys._getframe().f_back
        parent = frame
    
        bc = dis.Bytecode(parent.f_code)
        
        if name in _labels: # If label has already been discovered
            lineno = _labels[name]
            
        else: # Otherwise, search for it.
            # If the label is specified as "label .hello", we are looking for a pattern such as:
            #50 LOAD_GLOBAL              4 (label)
            #62 LOAD_ATTR                3 (hello)
            
            last_i_line = None # Last line specified by an instruction
            last_i = None # Last instruction
            
            for i in bc:
                if i.starts_line:
                    last_i_line = i.starts_line
                    
                if last_i is not None and last_i.opname in ('LOAD_GLOBAL', 'LOAD_NAME') and last_i.argval == 'label': # If last instruction was a "LOAD_GLOBAL label" ...
                    if i.opname == 'LOAD_ATTR': # ... AND current opperation is a LOAD_ATTR 
                        label_name = i.argval
                        _labels[label_name] = last_i_line
                        lineno = last_i_line
                        
                        if label_name == name:
                            break
                
                last_i = i

        if name not in _labels: # Label was not found
            raise UnknownLabel("No label named " + name)        
    
        # Switch line
        # Inspired from https://gist.github.com/georgexsh/ede5163a294ced53c3e2369ccaa392cc?permalink_comment_id=3291363#file-goto-py
        def hook(frame, event, arg):
            if event == 'line' and frame == parent:
                try:
                    frame.f_lineno = lineno
                except ValueError as e:
                    print("jump failed:", e)
                while frame:
                    frame.f_trace = None
                    frame = frame.f_back
                return None
            return hook
    
        while frame:
            frame.f_trace = hook
            frame = frame.f_back
        sys.settrace(hook)
        
goto = _goto()
    
    
    