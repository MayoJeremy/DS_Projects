import config as cfg
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen.canvas import Canvas
from random import randint


def watermarker(base_pdf: str, result_pdf: str):
    reader = PdfReader(cfg.DATADIR+base_pdf)
    writer = PdfWriter()
    page_indices = list(range(0, len(reader.pages)))
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        reader_foot_stamp = PdfReader(
            cfg.DATADIR+cfg.FOOTER_TEMPLATE_FILE.get("temp_file_name"))
        reader_stamp = PdfReader(
            cfg.DATADIR+cfg.STAMP_TEMPLATE_FILE.get("temp_file_name"))
        stamp_page = reader_stamp.pages[0]
        image_page = reader_foot_stamp.pages[0]

        image_page.merge_page(stamp_page)
        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(cfg.RESULTDIR+result_pdf, "wb") as fp:
        writer.write(fp)


def create_footer():
    create_watermark_template(**cfg.FOOTER_TEMPLATE_FILE)


def create_water_stamp():
    create_multipage_watermark_template(5, **cfg.STAMP_TEMPLATE_FILE)


def create_multipage_watermark_template(page_amt, temp_file_name, x_cord, y_cord,
                                        deg_rotation, font_name, font_size,
                                        font_color_rgb):
    canvas = Canvas(cfg.DATADIR + temp_file_name)
    x_cord_imp = x_cord
    y_cord_imp = y_cord
    for _ in range(page_amt):
        canvas.setFont(font_name, font_size)
        canvas.setFillColorRGB(*font_color_rgb.values())
        x_cord = randint(*x_cord_imp)
        y_cord = randint(*y_cord_imp)
        if deg_rotation:
            canvas.rotate(randint(0, deg_rotation))
            y_cord *= -1

        canvas.drawString(x=x_cord, y=y_cord, text=cfg.WATERTEXT)
        canvas.showPage()
    canvas.save()


def create_watermark_template(temp_file_name, x_cord, y_cord, deg_rotation,
                              font_name, font_size, font_color_rgb):
    canvas = Canvas(cfg.DATADIR + temp_file_name)

    canvas.setFont(font_name, font_size)
    canvas.setFillColorRGB(*font_color_rgb.values())
    if deg_rotation:
        canvas.rotate(deg_rotation)
        y_cord *= -1
    canvas.drawString(x=x_cord, y=y_cord, text=cfg.WATERTEXT)
    canvas.save()


def main():
    create_footer()
    create_water_stamp()
    watermarker("Watermark.pdf", "new_water.pdf")


if __name__ == "__main__":
    main()
