# """
# ToDo:
#     Root.py:
#         - implement New Config option in Menu
#         - Style:
#             - SelectModelFrame
#             - ConfigFrame
#             - FooterFrame
#             -




# """
# import View.Root
# import View.ModelSelectFrame
# import View.ConfigFrame
# import View.MainFrame
# import View.FooterFrame

# class FrameManager:

#     def __init__(self):
#         self.root = None


#     def mainFrame(self, cfg):
#         self.cfg = cfg
#         self.root = self.createWindow(self.cfgFrame)
#         self.root.createMenu(self)

#         self.mf = MainFrame(self)
#         self.cfgList = InitTileConfig(self)

#         self.tileFrame = self.getTileFrame(self.model, self.mf)
#         self.tileFrame.setTileList(self.cfgList.getButtons())
#         self.tileFrame.create()

#         self.mf.setContent(self.tileFrame)
#         self.mf.setFooter(FooterFrame(self))
#         self.mf.create()


#     def configFrame(self, model):

#         self.model = model

#         self.root = self.createWindow(self.msFrame)
#         self.root.setSize(500,800)
#         self.cfgFrame = ConfigFrame(self)
#         self.root.title(self.cfgFrame.title)
#         # self.root.mainloop()
#         # print("configFram called")

#     def selectModelFrame(self, frame):

#         self.root = self.createWindow(frame)

#         self.root.setSize(SELECT_MODEL_FRAME_WIDTH, SELECT_MODEL_FRAME_HEIGHT)
#         self.msFrame =  ModelSelectFrame(self)
#         self.root.title(self.msFrame.title)


#     def createWindow(self, frame):
#         if frame != None:
#             frame.destroy()
#         if self.root != None:
#             self.root.destroy()
#         root = Root()

#         return root

#     def startLoop(self):
#         self.root.mainloop()

#     def getPhoneModels(self):
#         return phoneModels

#     def getTileFrame(self, model, mf):
#         match(model):
#             case "Astra 6737i":
#                 return A37(mf)
#             case "Astra 6739i":
#                 return A39(mf)
#             case "Yealink T48":
#                 return T48(mf)
#             case "Yealink T46":
#                 return T46(mf)
#             case "Yealink T42":
#                 return T42(mf)
#             case "Yealink T41":
#                 return T42(mf)
#             case "Yealink EXP40":
#                 return EXP40(mf)





# fm = FrameManager()
# fm.selectModelFrame(None)
# fm.startLoop()
