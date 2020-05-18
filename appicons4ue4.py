import inkex
import os
from inkex.command import inkscape

class AppIcons(inkex.Effect):
    
    def __init__(self):
        super(AppIcons, self).__init__()
    
    def add_arguments(self, pars):
        pars.add_argument("--output_path", default=os.path.expanduser("~"), help="Existing output directory")
        pars.add_argument("--android", type=inkex.Boolean, help="If true will export icons for Android.")
        pars.add_argument("--ios", type=inkex.Boolean, help="If true will export icons for iOS.")
    
    def effect(self):
        
        if not os.path.isdir(self.options.output_path):
            os.makedirs(self.options.output_path);
        
        if(self.options.ios):
            self.export_image("icon57", 57)
            self.export_image("icon57@2x", 114)
            self.export_image("icon60@2x", 120)
            self.export_image("icon60@3x", 180)
            self.export_image("icon72", 72)
            self.export_image("icon72@2x", 144)
            self.export_image("icon76", 76)
            self.export_image("icon76@2x", 152)
            self.export_image("icon83.5@2x", 167)
            self.export_image("icon1024", 1024)
            self.export_image("icon20", 20)
            self.export_image("icon20@2x", 40)
            self.export_image("icon20@3x", 60)
            self.export_image("icon29", 29)
            self.export_image("icon29@2x", 58)
            self.export_image("icon29@3x", 87)
            self.export_image("icon40", 40)
            self.export_image("icon40@2x", 80)
            self.export_image("icon40@3x", 120)
            self.export_image("icon50", 50)
            self.export_image("icon50@2x", 100)
        if(self.options.android):
            self.export_image("android-ldpi", 36)
            self.export_image("android-mdpi", 48)
            self.export_image("android-hdpi", 72)
            self.export_image("android-xhdpi", 96)
            self.export_image("android-xxhdpi", 144)
            self.export_image("android-xxxhdpi", 192)
        
        
    def export_image(self, name, size):
        dir = self.options.output_path
        file = "{}.png".format(name)
        output_file=os.path.join(dir, file)
        kwargs = {'export-area': '0:0:108:108', 'export-filename': output_file,
                  'export-width': str(size), 'export-height': str(size)}
        inkscape(self.options.input_file, **kwargs)

if __name__ == '__main__':
    AppIcons().run()