#============================================================ 
# PROGRAMMER:........ William L. Bahn 
# USERID:............ WBAHN 
# COURSE:............ CSCI-410 
# TERM............... FALL 2013 
# ASSIGNMENT:........ PY03 
# FILENAME:.......... py03.py 
# PYTHON VERSION:.... 3.3.0 
#============================================================

#=================================================================
# Instructor's Solution
#=================================================================
        
from CS410_inst_py import hack2xml, io_files

#=================================================================
# xml2asm
#=================================================================

# This function will process an XML file by finding the first
# tag and extracting it and then processing that tag. Since
# the XML files (as we are defining them) should have exactly
# one top level tag, this is all that is needed to process the
# entire file (at this level of abstraction).

def xml2asm(i_filename, o_filename):

   files = io_files(i_filename, o_filename)

   xml_goto_next_tag(files)
   tag = xml_extract_tag(files)
   xml_tag(tag, files)

   files.close()
   
# xml_goto_next_tag() searches until it finds an opening
# angle bracket.

def xml_goto_next_tag(files):
   
   c = files.read()

   while ('<' != c):
      if ('' == c):
         print("EOF while looking for next XML tag.")
         quit()
      c = files.read()
   
# xml_extract_tag() assumes that the opening angle bracket
# has already been found. It reads the tag name and returns
# it. In the process, it reads the closing angle bracket.

def xml_extract_tag(files):
   
   c = files.read()

   tag = ''
   while ('>' != c):
      if ('' == c):
         print("EOF while reading XML tag.")
         quit()
      tag += c
      c = files.read()

   return tag

# xml_tag() accepts a tag name, along with the input and output
# files. It then walks through the file collecting the raw content
# (ignoring whitespace) and adding the content returned from any
# tags it encounters along the way. Once a closing tag is found,
# it is validated against the opening tag and, if they match, the
# appropriate tag function is called along with the contents that
# was collected.

def xml_tag(tag, files):
   
   contents = ''
   close_tag_found = False
   while (not close_tag_found):
      c = files.read()
      if ('<' == c): # tag encountered
         newtag = xml_extract_tag(files)
         if (newtag.startswith('/')):
            close_tag_found = True
            #print("CLOSE TAG: %s" % newtag)
         else:
            contents += xml_tag(newtag, files)
      else:
         if (not c.isspace()):
            contents += c   

   #print("Matching <%s> to <%s>" % (tag, newtag))
   if (newtag != ('/'+tag)):
      print("Mismatched XML tags.")
      quit()
      
   # xml_tag_test(contents, o_file)
   if (tag == "hack"):          contents = xml_tag_hack(contents, files)
   if (tag == "A-Instruction"): contents = xml_tag_atype(contents, files)
   if (tag == "C-Instruction"): contents = xml_tag_ctype(contents, files)
   if (tag == "address"):       contents = xml_tag_address(contents, files)
   if (tag == "constant"):      contents = xml_tag_constant(contents, files)
   if (tag == "comp"):          contents = xml_tag_comp(contents, files)
   if (tag == "dest"):          contents = xml_tag_dest(contents, files)
   if (tag == "jump"):          contents = xml_tag_jump(contents, files)

   return contents

# Each of the following functions processes the final contents of one
# particular tag type. The function is called only after the tag has
# been properly closed. The contents consists of the raw contents that
# was between the tags, as well as the content returned by any inter-
# vening tags.

def xml_tag_test(contents, files):

   print("Tag contents: <%s>" % contents)
   return contents

def xml_tag_hack(contents, files):

   return ''

def xml_tag_atype(contents, files):

   print("%s" % contents, end='')
   files.write("%s" % contents)

   return ''
   
def xml_tag_ctype(contents, files):

   for c in contents:
      print("%c" % c, end='')
      files.write("%c" % c)
      if (c == ':'):
         print(" 1 11", end='')
         files.write(" 1 11")

   return ''
   
def xml_tag_address(contents, files):

   address = int(contents)
   if (address):
      print('')
      files.write('\n')
   print("// ", end='')
   files.write("// ")
   contents = ("%05i:" % address)

   return contents
   
def xml_tag_constant(contents, files):

   value = int(contents)
   if ((value > 32767)or(value < 0)):
      print("Illegal value in <constant> tag.")
      quit()
      
   contents = ''
   for group in range(0,4):
      for bit in range(0,4):
         if (value%2):
            contents = '1'+contents
            value -= 1
         else:
            contents = '0'+contents
         value /= 2
      contents = ' '+contents

   return contents
   
def xml_tag_comp(contents, files):

   value = int(contents,16)
   if ((value > 128)or(value < 0)):
      print("Illegal value in <comp> tag.")
      quit()
      
   contents = ''
   for bit in range(0,7):
      if (bit == 6):
         contents = ' '+contents
      if (value%2):
         contents = '1'+contents
         value -= 1
      else:
         contents = '0'+contents
      value /= 2
   contents = ' '+contents

   return contents
   
def xml_tag_dest(contents, files):

   contents = (" %s" % contents)

   return contents
   
def xml_tag_jump(contents, files):

   contents = (" %s" % contents)

   return contents
   
#=================================================================
# MAIN:
#=================================================================

hack2xml("machine.hack", "machine.xml")
xml2asm("machine.xml", "assembly.asm")

#=================================================================

