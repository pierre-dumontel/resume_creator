from elements import TextVariables
import matplotlib.pyplot as plt
# %matplotlib inline

text = TextVariables()
# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'
fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#006400', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add text
plt.annotate(text.Header, (.02,.01), weight='regular', fontsize=8, alpha=0.9)
plt.annotate(text.Name, (.26,.96), weight='bold', fontsize=25)
plt.annotate(text.Contact, (.7,.93), weight='regular', fontsize=9, color='#ffffff')
plt.annotate(text.LinkedIn, (.7,.912), weight='regular', fontsize=9, color='#ffffff', url='https://www.linkedin.com/in/pierre-dumontel-ba0646178/')
plt.annotate(text.GitHub, (.7,.895), weight='regular', fontsize=9, color='#ffffff', url='https://www.github.com/pierre-dumontel')

plt.annotate(text.TitleHeader, (.02,.87), weight='bold', fontsize=10, color='#006400')
plt.annotate(text.TitleDesc, (.04,.815), weight='regular', fontsize=10)


# EXperiences
plt.annotate(text.WorkHeader, (.02,.79), weight='bold', fontsize=10, color='#006400')
plt.annotate(text.WorkOneTitle, (.02,.76), weight='bold', fontsize=10)
plt.annotate(text.WorkOneTime, (.04,.74), weight='regular', fontsize=9, alpha=.6)
plt.annotate(text.WorkOneDesc, (.04,.68), weight='regular', fontsize=10)

plt.annotate(text.WorkTwoTitle, (.02,.65), weight='bold', fontsize=10)
plt.annotate(text.WorkTwoTime, (.04,.63), weight='regular', fontsize=9, alpha=.6)
plt.annotate(text.WorkTwoDesc, (.04,.57), weight='regular', fontsize=10)

plt.annotate(text.WorkThreeTitle, (.02,.54), weight='bold', fontsize=10)
plt.annotate(text.WorkThreeTime, (.04,.52), weight='regular', fontsize=9, alpha=.6)
plt.annotate(text.WorkThreeDesc, (.04,.46), weight='regular', fontsize=10)

plt.annotate(text.WorkFourTitle, (.02,.43), weight='bold', fontsize=10)
plt.annotate(text.WorkFourTime, (.04,.41), weight='regular', fontsize=9, alpha=.6)
plt.annotate(text.WorkFourDesc, (.04,.35), weight='regular', fontsize=10)

# Education
plt.annotate(text.EduHeader, (.02,.31), weight='bold', fontsize=10, color='#006400')
plt.annotate(text.EduOneTitle, (.02,.26), weight='bold', fontsize=10)
plt.annotate(text.EduOneTime, (.04,.24), weight='regular', fontsize=9, alpha=.6)
plt.annotate(text.EduOneDesc, (.04,.125), weight='regular', fontsize=10)
plt.annotate(text.EduTwoTitle, (.02,.095), weight='bold', fontsize=10)
plt.annotate(text.EduTwoTime, (.04,.075), weight='regular', fontsize=9, alpha=.6)
plt.annotate(text.EduTwoDesc, (.04,.035), weight='regular', fontsize=10)

#Skills
plt.annotate(text.SkillsHeader, (.7,.8), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(text.SkillsDesc, (.7,.49), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(text.FuncSkillsHeader, (.7,.44), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(text.FuncSkillsDesc, (.7,.3), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(text.SoftSkillsHeader, (.7,.25), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(text.SoftSkillsDesc, (.7,.185), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(text.AboutMeHeader, (.7,.13), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(text.AboutMeDesc, (.7,.065), weight='regular', fontsize=10, color='#ffffff')


from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
arr_code = mpimg.imread('my_picture.jpg')
imagebox = OffsetImage(arr_code, zoom=0.07)
ab = AnnotationBbox(imagebox, (0.12, 0.97))
ax.add_artist(ab)

plt.savefig('cv_pdumontel_vf.pdf', dpi=300, bbox_inches='tight')
