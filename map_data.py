from models import Color, Line

white = Color(255, 255, 255)

lines = {
    'Jubilee': Line(name='Jubilee', bg_color=Color(104, 110, 114), fg_color=white),
    'Bakerloo': Line(name='Bakerloo', bg_color=Color(174, 97, 24), fg_color=white),
    'Central': Line(name='Central', bg_color=Color(228, 31, 31), fg_color=white),
    'District': Line(name='District' , bg_color=Color(0, 114, 41), fg_color=white),
    'Piccadilly': Line(name='Piccadilly', bg_color=Color(4, 80, 161), fg_color=white),
    'Victoria': Line(name='Victoria', bg_color=Color(0, 159, 224), fg_color=white),
    'Hammersmith and City': Line(name='Hammersmith and City', bg_color=Color(232, 153, 168), fg_color=Color(17, 56, 146)),
    'Waterloo and City': Line(name='Waterloo and City', bg_color=Color(112, 195, 206), fg_color=Color(17, 56, 146)),
    'Circle': Line(name='Circle', bg_color=Color(248, 212, 45), fg_color=Color(17, 56, 146)),
    'Northern': Line(name='Northern', bg_color=Color(0, 0, 0), fg_color=white),
    'Metropolitan': Line(name='Metropolitan', bg_color=Color(137,50,103), fg_color=white),
    'Overground': Line(name='Overground', bg_color=Color(255,136,102), fg_color=white),
    'DLR': Line(name='DLR', bg_color=Color(0,187,180), fg_color=white),
}