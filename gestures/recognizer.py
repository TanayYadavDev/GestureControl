class GestureRecognizer:

    def __init__(self):
        pass

    def recognize(self, fingers):

        if fingers == [1,1,1,1,1]:
            return "OPEN_PALM"

        elif fingers == [0,0,0,0,0]:
            return "FIST"

        elif fingers == [0,1,0,0,0]:
            return "POINT"

        elif fingers == [0,1,1,0,0]:
            return "PEACE"

        elif fingers == [1,0,0,0,0]:
            return "THUMBS_UP"
        
        elif fingers == [0,1,0,0,1]:
            return "VICTORY"

        return "UNKNOWN"