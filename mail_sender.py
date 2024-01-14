from reportlab.pdfgen.canvas import Canvas


def create_cover_letter(cov_str):
    canvas          = Canvas("Cover_Letter.pdf")
    cov_str         = cov_str.replace("ı","i")
    cov_str_lines   = cov_str.splitlines( )
    # 70*12 x 50*12
    # 38 chars per line
    canvas.drawString(72, 61*12, cov_str_lines[0])
    line_counter    = 0
    line_char_count = 38
    for i in cov_str_lines[1:]:
        canvas.drawString(72, (60-line_counter)*12, cov_str[line_counter*line_char_count:len(cov_str)])
        line_counter += 1
    canvas.save()

def send(email_dict):
    create_cover_letter(email_dict["cover_letter"])