


#to export the data
@csrf_exempt
def Export(request):
        global username
        global username1
        username1=username
        print "USERENAMWE IN CREATEUSER",username
        obj_session = shriaccess3.Admin_sessionid()
        flag=obj_session.session_validation(username)
        print "FLAF VALJISDBH SHNDFONSK FHSOIJDFLSDFS",flag
        if (flag):
                Product=request.POST["Product"]
                Release=request.POST["release"]
                Build=request.POST['build']
                Export=request.POST["PDF"]  

                product = remove_unary(Product)
                product1=product.lower()
                release = remove_unary(Release)
                build = remove_unary(Build)
                export = remove_unary(Export)
                        
                print "product in export======",product
                print "release in export======",release
                print "build in export======",build
                print "export in export======",export

                list_checkBox = []
                list_checkBox1 = []

                temp = request.POST.getlist('module')
                print "temp in export------------=",temp
                for i in range(len(temp)):
                        temp1 = remove_unary(temp[i])
                        list_checkBox1.append(temp1)

                print "modules checked = ",list_checkBox1
                print "length of list_checkBox1->",len(list_checkBox1)
                if len(list_checkBox1) == 1:
                        list_checkBox1=str(list_checkBox1[0])
                else:
                        list_checkBox1=str(list_checkBox1)

                Module=list_checkBox1
                Module = Module.lower()
                print "Module in export-----------------------------=",Module

                list_run=[]
                list_run.append(product1)
                list_run.append(release)
                list_run.append(build)
                list_run.append(Module)
                print "list_run============================================",list_run

                list_testid = []
                list_testid.append(product)
                list_testid.append(Module)
                list_testid.append(release)
                list_testid.append(build)
                print "list_testid=============================================",list_testid
                        
                #fetching runs for the selected data
                obj = shriaccess3.testexecution()
                run = obj.run('fetch',list_run)
                run2=sorted(run)
                print "runs fetched for data in export========================",run
                j=len(run)-1
                run_lat = run[j]
                print "latest run___________________",run_lat
                        

                #fetching the status results and testcases for the latest run
                run1=[]
                run1.append(run_lat)
                #status
                status = obj.status('fetch',run1)
                print "status fetched for latest run in export______________",status

                #testcases
                tid = obj.testcaseid('fetch',run1)
                print "testcases fetched in export_______________",tid 
                        
                pass_var = 0
                fail_var=0
                exc=0

                for i in status:
                        if i == "pass":
                                pass_var = pass_var+1
                        else:
                                fail_var=fail_var+1

                print "no of pass===========",pass_var
                print "no of fail===========",fail_var

                server_path_views = os.getcwd()
                if (Export=='PDF'):
                        dummy1=[]
                        dummy2=[]

                        header = [('TESTCASES','STATUS (PASS/FAIL)')]
                                
                        k = process(tid,status,dummy1,dummy2)      #process takes 4 arguments, so providing two dummy values
                        print "value k in export______________",k

                        k = header + k
                                
                        name = "Report_for_" + str(product) + "_" + str(release) + "_" + str(build) + "_" + str(Module) + ".pdf"
                        print "name====",name
                        doc = SimpleDocTemplate(name,pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=60)
                         
                        report = []
                        data = []
                        styles = getSampleStyleSheet()
                        styles.add(ParagraphStyle(name='Bold', fontSize=10, leading = 15, alignment=TA_LEFT))
                        t=Table(k,colWidths=[200,200],hAlign='LEFT')
                        t.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
                        ('TEXTCOLOR',(1,1),(-2,-2),colors.black),
                        ('VALIGN',(0,0),(0,-1),'TOP'),
                        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                        ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                        ]))

                                ########## For Graph##########
                        dr = Drawing(300, 300)
                        graph=Pie()
                        graph.x = 50
                        graph.y = 50
                        graph.width = 225
                        graph.height = 225
                        graph.data = [pass_var,fail_var,exc]
                        graph.labels = ['Pass','Fail','No_Run']
                        dr.add(graph)
                        dr.save(formats=['bmp'],outDir='.',fnRoot=None)

                        im = Image("Drawing000.bmp")
                        im.hAlign = 'LEFT'


                        report.append(Paragraph("Selected Product details.." ,styles["Bold"]))
                        report.append(Paragraph("Product      : "+product,styles["Bold"]))
                        report.append(Paragraph("Module : "+Module,styles["Bold"]))
                        report.append(Paragraph("Release : "+Release,styles["Bold"]))
                        report.append(Paragraph("Build : "+Build,styles["Bold"]))
                        report.append(Paragraph("-------------------------------------------",styles["Bold"]))
                        report.append(Paragraph(" ",styles["Bold"]))
                        report.append(Paragraph("Project Detailed Status ." ,styles["Bold"]))
                        report.append(Paragraph("           ",styles["Bold"]))
                        report.append(t)
                        report.append(Paragraph("-------------------------------------------",styles["Bold"]))
                        report.append(Paragraph("Pie chart." ,styles["Bold"]))
                        report.append(im)

                        # Build Document
                        doc.build(report)
                        val="Converted to Pdf"

                        #download
                        file_path =os.getcwd()+'//'+ name
                        print "file pth_________",file_path
                        file_wrapper = FileWrapper(file(file_path,'rb'))
                        print "file wrap____________",file_wrapper
                        file_mimetype = mimetypes.guess_type(file_path)
                        print "mime type_____________",file_mimetype
                        response = HttpResponse(file_wrapper, content_type=file_mimetype )
                        response['X-Sendfile'] = file_path
                        response['Content-Length'] = os.stat(file_path).st_size
                        nameOnly = name.split('/')
                        response['Content-Disposition'] = 'attachment; filename=%s' % nameOnly[len(nameOnly)-1] 
                        return response

                ##                return render_to_response('thanks.html',{'var':val})
                 
                elif(Export == 'XLS'):
                        dummy1=[]
                        dummy2=[]

                        header = [('TESTCASES','STATUS (PASS/FAIL)')]
                                
                        k = process(tid,status,dummy1,dummy2)      #process takes 4 arguments, so providing two dummy values
                        print "value k in export______________",k

                        k = header + k

                        ########## For Graph##########
                        dr = Drawing(300, 300)
                        graph=Pie()
                        graph.x = 50
                        graph.y = 50
                        graph.width = 225
                        graph.height = 225
                        graph.data = [pass_var,fail_var,exc]
                        graph.labels = ['Pass','Fail','No_Run']
                        dr.add(graph)
                        dr.save(formats=['bmp'],outDir='.',fnRoot=None)

                        im = Image("Drawing000.bmp")
                        im.hAlign = 'LEFT'

                        book = xlwt.Workbook(encoding="utf-8")
                        sheet1 = book.add_sheet("Sheet 1")
                        i=0
                        j=0
                ##                for i, row in enumerate(k):
                ##                        for j, col in enumerate(row):
                ##                                sheet1.write(i, j, col)
                ##                                sheet1.col(0).width = 256 * max([len(row[0]) for row in k])
                ##
                ##
                ##                sheet1.write(i+3,j-1,"Product")
                ##                sheet1.write(i+4,j-1,"Release")
                ##                sheet1.write(i+5,j-1,"Build")
                ##                sheet1.write(i+6,j-1,"Module")
                ##                
                ##                sheet1.write(i+3,j,product)
                ##                sheet1.write(i+4,j,release)
                ##                sheet1.write(i+5,j,build)
                ##                sheet1.write(i+6,j,Module)


                        sheet1.write(i,j,"Product")
                        sheet1.write(i+1,j,"Release")
                        sheet1.write(i+2,j,"Build")
                        sheet1.write(i+3,j,"Module")
                                
                        sheet1.write(i,j+1,product)
                        sheet1.write(i+1,j+1,release)
                        sheet1.write(i+2,j+1,build)
                        sheet1.write(i+3,j+1,Module)

                        i=i+6

                        for row in k:
                                j=0
                                for col in row:
                                        sheet1.write(i, j, col)
                                        sheet1.col(0).width = 256 * max([len(row[0]) for row in k])
                                        j=j+1
                                i=i+1


                        sheet1.insert_bitmap('Drawing000.bmp',2,5 )
                        name1 = "Report_for_" + str(product) + "_" + str(release) + "_" + str(build) + "_" + str(Module) + ".xls"
                ##                dest_path = server_path_views + "\\Report_" + str(product) + "_" + str(release) + "_" + str(build) + "_" + str(Module) + ".xls"
                        file_path =os.getcwd()+'//'+ name1
                        book.save(file_path)
                        val="Converted to XLS"

                                #download
                ##                file_path =os.getcwd()+'//'+ dest_path
                        print "file pth_________",file_path
                        file_wrapper = FileWrapper(file(file_path,'rb'))
                        print "file wrap____________",file_wrapper
                        file_mimetype = mimetypes.guess_type(file_path)
                        print "mime type_____________",file_mimetype
                        response = HttpResponse(file_wrapper, content_type=file_mimetype )
                        response['X-Sendfile'] = file_path
                        response['Content-Length'] = os.stat(file_path).st_size
                        nameOnly = name1.split('/')
                        response['Content-Disposition'] = 'attachment; filename=%s' % nameOnly[len(nameOnly)-1] 
                        return response

                                
                ##                return render_to_response('thanks.html',{'var':val})
                elif(Export =='CVS'):
                        return render_to_response('thanks.html')
                else:
                        return render_to_response('thanks.html')
        else:
                return render_to_response('loginpage.html')
