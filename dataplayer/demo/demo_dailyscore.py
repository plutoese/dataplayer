# coding=UTF-8

from libs.class_Excel import Excel

filename = r'd:\data\econometrics_normal.xlsx'
mexcel = Excel(filename)
mexcel.read()
rdata = mexcel.data
print(rdata)

# 基本算法
# score = 63 + 4*3 + 3*8

result = []
for row in rdata[1:]:
    score = 50 + int(row[5])*4 + int(row[6])*4 + int(row[7])*4 + int(row[8])*4 \
            + int(row[9])*2 + int(row[10])*2 + int(row[11])*2 + int(row[12])*2
    rowdata = row
    rowdata.append(score)
    result.append(rowdata)

outfile = r'd:\data\econometrics_score2.xlsx'
moutexcel = Excel(outfile)
moutexcel.new().append(result, 'mysheet')
moutexcel.close()