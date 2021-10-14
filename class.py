
# Object for all class items
class school_class():
    def __init__(self,name,professor,section,*time):
        self.name = name
        self.professor = professor
        self.section = section
        self.times = list()
        for t in time:
            self.times.add(t)

    def get_name(self) -> str:
        pass

    def get_professor(self)-> str:
        pass

    def get_section(self)-> str:
        pass

    def get_times(self) -> list:
        pass

    def set_zoom_link(self, s: str) -> None:
        self.zoom_link = s

    def get_zoom_link(self) -> str:
        pass

    def dump_info(self) -> list:
        c_name = self.get_name + "-" + self.get_section
        ret_list = [c_name]
        data_list = [self.get_name,self.get_professor,self.get_section,self.get_times,self.get_zoom_link]
        ret_list.append(data_list)
        return(ret_list)
