import os
import struct
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOGO = ROOT / 'images' / 'aimtolearnlogo.jpeg'
DOWNLOADS = ROOT / 'downloads'
DOWNLOADS.mkdir(exist_ok=True)

CONTENT = {
    'my-best-friend': {
        'title': 'My Best Friend',
        'text': '''
**Quote:** *“A true friend is the greatest of all blessings.”* — **François de La Rochefoucauld**

Friendship is one of the most beautiful gifts of life. It is a bond built on love, trust, care, and understanding. Everyone needs a true friend who stands by them in every situation. A best friend is someone who shares our happiness, supports us in difficult times, and makes our life more meaningful. School life becomes more enjoyable because of the friends we make, and the memories created with them remain in our hearts forever.

**Quote:** *“A friend is someone who knows all about you and still loves you.”* — **Elbert Hubbard**

My best friend is a kind, honest, and caring person. We have been together for many years, and our friendship grows stronger every day. We trust each other and respect each other's opinions. We never judge one another and always encourage each other to become better. Whether it is a happy moment or a difficult one, we are always there to support one another.

**Quote:** *“Friendship doubles our joy and divides our sorrow.”* — **Marcus Tullius Cicero**

We spend most of our time together at school. We sit in the same classroom, study together, complete assignments, and help each other understand difficult lessons. Whenever one of us faces a problem in studies, the other is always ready to explain it with patience. Learning becomes easier and more enjoyable when we work together because we motivate each other to perform our best.

**Quote:** *“The happiest moments in life are those shared with friends.”* — **Unknown**

Apart from studying, we also enjoy playing together during recess and after school. We participate in different games, sports, and school activities. Sometimes we compete with each other, but we always appreciate each other's efforts. We laugh, tell jokes, and create wonderful memories that make our friendship even stronger. These joyful moments bring happiness to our everyday lives.

**Quote:** *“The future belongs to those who believe in the beauty of their dreams.”* — **Eleanor Roosevelt**

One of the best parts of our friendship is that we dream together. We often talk about our future careers, our goals, and the kind of people we want to become. We encourage each other to work hard, stay focused, and never give up. Whenever one of us feels discouraged, the other offers hope and motivation. We believe that with dedication and mutual support, our dreams can become reality.

**Quote:** *“True friendship is built on trust, respect, and understanding.”* — **Unknown**

Like every friendship, we sometimes have small disagreements. However, we never allow misunderstandings to damage our relationship. We solve our problems through honest conversation and forgive each other quickly. This teaches us the importance of patience, kindness, and respect. Our friendship has helped us become more responsible, caring, and mature individuals.

**Quote:** *“Friends are the family we choose for ourselves.”* — **Edna Buchanan**

My best friend has taught me many valuable lessons about life. From sharing and caring to honesty and teamwork, every experience with my friend has made me a better person. We celebrate each other's achievements, support each other during failures, and stand together through every challenge. I feel truly fortunate to have such a wonderful companion who fills my life with happiness and confidence.

**Quote:** *“A sweet friendship refreshes the soul.”* — **Proverbs 27:9**

In conclusion, a best friend is one of life's greatest treasures. True friendship is not measured by the number of years spent together but by the love, trust, and unforgettable memories shared. I hope our friendship remains strong throughout our lives. No matter where the future takes us, I will always cherish the moments we spent studying together, playing together, dreaming together, and growing together. A true best friend is a priceless gift that stays in our heart forever.
'''
    },
    'television': {
        'title': 'Television',
        'text': '''
**Quote:** *“Knowledge is power.”* — **Francis Bacon**

Television is one of the most useful inventions of modern science. It is found in almost every home and is loved by people of all ages. It is not only a source of entertainment but also a great source of knowledge and information. Television brings the whole world into our living room. We can watch news, sports, movies, cartoons, documentaries, and educational programs with just the press of a button.

**Quote:** *“Learning never exhausts the mind.”* — **Leonardo da Vinci**

The first successful television was demonstrated by **John Logie Baird** in **1926**. In the beginning, televisions had only black-and-white screens. As technology improved, color televisions were introduced, followed by LED, Smart TVs, and Ultra HD televisions. Today, modern televisions provide excellent picture quality and many useful features, making learning and entertainment more enjoyable than ever.

**Quote:** *“Education is the key to success.”* — **Common Saying**

Television plays an important role in education. Students can learn many new things by watching educational channels and documentaries. Science experiments, history programs, language lessons, and nature shows make learning interesting and easy. Educational programs explain difficult concepts in a simple and engaging way. They also improve our general knowledge by teaching us about different countries, cultures, inventions, and famous personalities. Many students watch educational channels to strengthen their classroom learning and prepare for exams. In this way, television has become an important learning tool for people of all ages.

**Quote:** *“Laughter is the best medicine.”* — **Common Proverb**

One of the main reasons people watch television is entertainment. It offers different types of programs such as dramas, cartoons, movies, sports, cooking shows, quiz shows, and music programs. Every member of the family can find something they enjoy. Watching television together also gives families a chance to spend quality time with one another. Live broadcasts of cricket matches, award shows, and national celebrations make people feel connected even while sitting at home. Television provides relaxation after a busy day and helps reduce stress through enjoyable and meaningful programs.

**Quote:** *“Stay informed, stay prepared.”* — **Common Saying**

Television also keeps us updated with the latest news from around the world. We can learn about weather forecasts, scientific discoveries, sports events, and important national and international news. It also spreads awareness about health, road safety, environmental protection, and other social issues. In times of emergencies, television provides quick and reliable information to the public. Many government announcements and educational campaigns are also broadcast on television to guide and inform citizens. By watching authentic news channels, people become more aware of the world and can make better decisions in their daily lives.

**Quote:** *“Excess of everything is bad.”* — **Common Proverb**

Although television has many advantages, watching it for long hours can be harmful. It may affect our eyesight, reduce physical activity, and waste valuable time. Children may also lose interest in studies or outdoor games if they watch too much television. Therefore, we should watch television for a limited time and choose useful and educational programs. Parents should also monitor the programs their children watch to ensure they are suitable for their age. A balanced routine of study, exercise, and limited screen time helps maintain both physical and mental health.

**Quote:** *“Technology is a useful servant but a dangerous master.”* — **Christian Lous Lange**

Today, Smart TVs have made television even more useful. People can watch online classes, educational videos, documentaries, and live events through the internet. They can also connect with different learning platforms and enjoy high-quality programs. If used wisely, television can help us improve our knowledge and skills. Modern televisions also allow families to enjoy movies and educational content together, making learning more interactive and enjoyable. With continuous technological advancements, television is becoming smarter and more beneficial every year.

**Quote:** *“Use things, don't let things use you.”* — **Common Saying**

In conclusion, television is a wonderful invention that makes our lives easier, more enjoyable, and more informative. It entertains us, educates us, and keeps us connected with the world. Like every invention, it should be used wisely and in moderation. If we use television properly, it can become one of our best teachers and a valuable companion throughout life. It teaches us new ideas, broadens our thinking, and helps us understand different cultures and societies. Therefore, we should make television a source of learning and inspiration rather than merely a means of passing time.
'''
    }
}

XML_TEMPLATE = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n{body}'''

NAMESPACES = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'v': 'urn:schemas-microsoft-com:vml',
    'o': 'urn:schemas-microsoft-com:office:office',
    'm': 'http://schemas.openxmlformats.org/officeDocument/2006/math',
}


def escape_xml(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def make_docx(title, paragraphs, output_path):
    document_xml = []
    document_xml.append('<w:document xmlns:w="{w}" xmlns:r="{r}">'.format(**NAMESPACES))
    document_xml.append('<w:body>')
    document_xml.append('<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:b/></w:rPr><w:t>{}</w:t></w:r></w:p>'.format(escape_xml(title)))
    document_xml.append('<w:p/>')
    for paragraph in paragraphs:
        if paragraph.startswith('**Quote:**'):
            quote = paragraph[len('**Quote:**'):].strip()
            document_xml.append('<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:rPr><w:i/></w:rPr><w:t>{}</w:t></w:r></w:p>'.format(escape_xml(quote)))
        else:
            document_xml.append('<w:p><w:r><w:t>{}</w:t></w:r></w:p>'.format(escape_xml(paragraph)))
    document_xml.append('<w:sectPr>')
    document_xml.append('<w:pgSz w:w="11906" w:h="16838"/>')
    document_xml.append('<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/>')
    document_xml.append('<w:headerReference w:type="default" r:id="rIdHeader"/>')
    document_xml.append('<w:footerReference w:type="default" r:id="rIdFooter"/>')
    document_xml.append('</w:sectPr>')
    document_xml.append('</w:body></w:document>')
    document_xml = XML_TEMPLATE.format(body=''.join(document_xml))

    header_xml = XML_TEMPLATE.format(body='''<w:hdr xmlns:w="{w}" xmlns:r="{r}" xmlns:v="{v}" xmlns:o="{o}">
  <w:p>
    <w:r>
      <w:pict>
        <v:shape id="_x0000_s1025" type="#_x0000_t75" style="position:absolute;margin-left:0;margin-top:0;width:450pt;height:450pt;rotation:0;z-index:-251654144;opacity:0.1;">
          <v:imagedata r:id="rIdImage" o:title="Watermark"/>
        </v:shape>
      </w:pict>
    </w:r>
  </w:p>
</w:hdr>'''.format(**NAMESPACES))

    footer_xml = XML_TEMPLATE.format(body='''<w:ftr xmlns:w="{w}" xmlns:r="{r}">
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:r>
      <w:fldChar w:fldCharType="begin"/>
    </w:r>
    <w:r>
      <w:instrText xml:space="preserve"> PAGE </w:instrText>
    </w:r>
    <w:r>
      <w:fldChar w:fldCharType="separate"/>
    </w:r>
    <w:r>
      <w:t>1</w:t>
    </w:r>
    <w:r>
      <w:fldChar w:fldCharType="end"/>
    </w:r>
  </w:p>
</w:ftr>'''.format(**NAMESPACES))

    styles_xml = XML_TEMPLATE.format(body='''<w:styles xmlns:w="{w}">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:rPr>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
      <w:sz w:val="24"/>
      <w:szCs w:val="24"/>
    </w:rPr>
  </w:style>
</w:styles>'''.format(**NAMESPACES))

    core_xml = XML_TEMPLATE.format(body='''<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>{}</dc:title>
  <dc:creator>AIM TO LEARN</dc:creator>
  <cp:revision>1</cp:revision>
</cp:coreProperties>'''.format(escape_xml(title)))

    app_xml = XML_TEMPLATE.format(body='''<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>AIM TO LEARN</Application>
</Properties>''')

    content_types = XML_TEMPLATE.format(body='''<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Default Extension="jpeg" ContentType="image/jpeg"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>
  <Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>''')

    rels_xml = XML_TEMPLATE.format(body='''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>''')

    doc_rels_xml = XML_TEMPLATE.format(body='''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rIdHeader" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>
  <Relationship Id="rIdFooter" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
</Relationships>''')

    header_rels_xml = XML_TEMPLATE.format(body='''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rIdImage" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/image1.jpeg"/>
</Relationships>''')

    with zipfile.ZipFile(output_path, 'w', compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr('[Content_Types].xml', content_types)
        docx.writestr('_rels/.rels', rels_xml)
        docx.writestr('docProps/core.xml', core_xml)
        docx.writestr('docProps/app.xml', app_xml)
        docx.writestr('word/document.xml', document_xml)
        docx.writestr('word/styles.xml', styles_xml)
        docx.writestr('word/header1.xml', header_xml)
        docx.writestr('word/footer1.xml', footer_xml)
        docx.writestr('word/_rels/document.xml.rels', doc_rels_xml)
        docx.writestr('word/_rels/header1.xml.rels', header_rels_xml)
        if LOGO.exists():
            docx.write(LOGO, 'word/media/image1.jpeg')


def jpeg_dimensions(path):
    with open(path, 'rb') as f:
        data = f.read()
    i = 0
    if data[0:2] != b'\xff\xd8':
        raise ValueError('Not JPEG')
    i = 2
    while i < len(data):
        while data[i] == 0xFF:
            i += 1
        marker = data[i]
        i += 1
        length = struct.unpack('>H', data[i:i+2])[0]
        if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            i += 2
            bits = data[i]
            height = struct.unpack('>H', data[i+1:i+3])[0]
            width = struct.unpack('>H', data[i+3:i+5])[0]
            return width, height
        i += length - 2
    raise ValueError('JPEG SOF not found')


def make_pdf(title, paragraphs, output_path):
    page_width = 595.276
    page_height = 841.89
    margin = 40
    line_height = 16
    max_width = page_width - 2 * margin

    text_lines = []
    for paragraph in paragraphs:
        if paragraph.startswith('**Quote:**'):
            text_lines.append(('quote', paragraph[len('**Quote:**'):].strip()))
        else:
            text_lines.append(('body', paragraph.strip()))

    def wrap(text, max_chars=80):
        words = text.split(' ')
        lines = []
        line = ''
        for word in words:
            if len(line) + len(word) + 1 > max_chars:
                lines.append(line.strip())
                line = word + ' '
            else:
                line += word + ' '
        if line.strip():
            lines.append(line.strip())
        return lines

    pages = []
    current = []
    y = page_height - margin - 40
    for kind, text in text_lines:
        if kind == 'quote':
            wrapped = wrap(text, 70)
            if y - (len(wrapped) * line_height + 24) < margin + 40:
                pages.append(current)
                current = []
                y = page_height - margin - 40
            current.append(('quote', wrapped))
            y -= len(wrapped) * line_height + 24
        else:
            wrapped = wrap(text, 90)
            if y - (len(wrapped) * line_height + 16) < margin + 40:
                pages.append(current)
                current = []
                y = page_height - margin - 40
            current.append(('body', wrapped))
            y -= len(wrapped) * line_height + 16
    if current:
        pages.append(current)

    with open(output_path, 'wb') as f:
        objs = []
        def obj(num, data):
            objs.append((num, data))

        def pdf_string(s):
            return '({})'.format(s.replace('(', '\(').replace(')', '\)').replace('\\', '\\'))

        # image object
        image_bytes = LOGO.read_bytes() if LOGO.exists() else b''
        img_w, img_h = jpeg_dimensions(LOGO) if LOGO.exists() else (1, 1)
        obj(1, b'<< /Type /Catalog /Pages 2 0 R >>')
        page_objs = []
        for i, page in enumerate(pages, start=1):
            page_objs.append(i+1)
        # resources
        font_obj = len(pages) + 3
        image_obj = font_obj + 1
        gs_obj = image_obj + 1
        content_objs = []
        for i, page in enumerate(pages, start=1):
            content_objs.append(gs_obj + i)
        # create page objects later
        for i, page in enumerate(pages, start=1):
            contents = []
            contents.append('q
0.12 w
0.75 0.75 0.75 RG
0.75 0.75 0.75 rg
1 0 0 1 0 0 cm
/GS1 gs
BI
/Im1 Do
Q
')
            contents.append('BT
/F1 18 Tf
1 0 0 1 {x} {y} Tm
{}'.format(pdf_string(page_title(title))) .replace('{x}', str(margin).replace('.0','')).replace('{y}', str(page_height - margin - 20).replace('.0','')))
            # Actually page_title not defined? We'll fix below.
            f
        

