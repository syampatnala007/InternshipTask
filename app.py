from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    file=''
    start_line=''
    end_line=''
    if request.method=='GET':
        file=request.args.get('file')
        start_line=request.args.get('start_line')
        end_line=request.args.get('end_line')
        if file=='' or file==None:
            file='file1.txt'
        chart='utf-8'
        if str(file)=='file4.txt':
            chart='utf-16'
        if (start_line=='' and end_line=='') or (start_line==None and end_line==None):
            try:
                s=[]
                with open(str(file),'r',encoding=chart,errors='ignore') as x:
                    s=x.readlines()
                    return render_template('index.html',file=s,fname=file)
            except:
                return 'File Not found!! Please enter a valid file name..'
        else:
            try:
                with open(str(file),'r',encoding=chart,errors='ignore') as x:
                    s=[]
                    tmp=x.readlines()
                    if (start_line=='' or start_line==None) and (end_line!='' and end_line!=None):
                        start_line='0'
                    if (start_line!='' and start_line!=None) and (end_line=='' or end_line==None):
                        file_length=len(tmp)
                        end_line=str(file_length)
                        print("hai",end_line)
                    if int(start_line)>int(end_line):
                        return 'Start line number must be less than or equal to the End line Number'
                    if int(start_line)<0 or int(end_line)<0:
                        return 'Line numbers cant be negative'
                    if int(end_line)<len(tmp):
                        for i in range(int(start_line),int(end_line)+1):
                            s.append(tmp[i])
                    else:
                        for i in range(int(start_line),int(end_line)):
                            s.append(tmp[i])
                    return render_template('index.html',file=s,fname=file)
            except ValueError:
                return 'Start line (start_line) and end line (end_line) should be numbers only'
            except FileNotFoundError:
                return 'File Not found!! Please enter a valid file name..'
            except IndexError:
                return 'Start or End lines limit exceeded or not within limits!'

if __name__=="__main__":
    app.run(debug=True)