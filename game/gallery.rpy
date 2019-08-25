define locked_gallery = "gui/button/gallery_locked.png"
define idle_gallery = "gui/button/gallery_idle.png"
define hover_gallery = "gui/button/gallery_hover.png"

define naoko__gallery_1 = "images/gallery/gallery_naoko_sex1.png"
define touko_aina__gallery_1 = "images/gallery/gallery_touko_aina_sex1.png"
define touko_aina__gallery_2 = "images/gallery/gallery_touko_aina_sex1.png"
define touko_aina__gallery_3 = "images/gallery/gallery_touko_aina_sex1.png"
define touko_aina__gallery_4 = "images/gallery/gallery_touko_aina_sex1.png"
define touko_aina__gallery_5 = "images/gallery/gallery_touko_aina_sex1.png"
define touko_aina__gallery_6 = "images/gallery/gallery_touko_aina_sex1.png"
define ritsuko__gallery_1 = "images/gallery/gallery_ritsuko_sex1.png"
define ritsuko__gallery_2 = "images/gallery/gallery_ritsuko_sex1.png"
define ritsuko__gallery_3 = "images/gallery/gallery_ritsuko_sex1.png"
define ritsuko__gallery_4 = "images/gallery/gallery_ritsuko_sex1.png"
define rina__gallery_1 = "images/gallery/gallery_rina_sex1.png"
define rina__gallery_2 = "images/gallery/gallery_rina_sex2.png"
define rina__gallery_3 = "images/gallery/gallery_rina_sex2.png"
define rina__gallery_4 = "images/gallery/gallery_rina_sex2.png"

default gallery_page = "naoko"

init python:
    def SetGalleryPage(page):
        global gallery_page
        gallery_page = page

screen gallery:
    tag menu
    
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(_("Gallery")):

        fixed:

            grid 3 2:

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                # Naoko Scene
                if gallery_page == "naoko":
                    if persistent.naoko__cg_1:
                        imagebutton action Replay("naoko__cg_1"):
                            background naoko__gallery_1
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery
                    
                    null
                    null

                    null
                    null
                    null

                # Rina Scenes
                if gallery_page == "rina":
                    if persistent.rina__cg_1:
                        imagebutton action Replay("rina__cg_1"):
                            background rina__gallery_1
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                    if persistent.rina__cg_2:
                        imagebutton action Replay("rina__cg_2"):
                            background rina__gallery_2
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                    if persistent.rina__cg_3:
                        imagebutton action Replay("rina__cg_3"):
                            background rina__gallery_3
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery


                    if persistent.rina__cg_4:
                        imagebutton action Replay("rina__cg_4"):
                            background rina__gallery_4
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery
                    null
                    null
                # Aina/Touko Scenes
                if gallery_page == "aina":
                    if persistent.touko_aina__cg_1:
                        imagebutton action Replay("touko_aina__cg_1"):
                            background touko_aina__gallery_1
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                    if persistent.touko_aina__cg_2:
                        imagebutton action Replay("touko_aina__cg_2"):
                            background touko_aina__gallery_2
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                    if persistent.touko_aina__cg_3:
                        imagebutton action Replay("touko_aina__cg_3"):
                            background touko_aina__gallery_3
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                    
                    if persistent.touko_aina__cg_4:
                        imagebutton action Replay("touko_aina__cg_4"):
                            background touko_aina__gallery_4
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                    if persistent.touko_aina__cg_5:
                        imagebutton action Replay("touko_aina__cg_5"):
                            background touko_aina__gallery_5
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                    if persistent.touko_aina__cg_6:
                        imagebutton action Replay("touko_aina__cg_6"):
                            background touko_aina__gallery_6
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                # Ritsuko Scenes
                if gallery_page == "ritsuko":
                    if persistent.ritsuko__cg_1:
                        imagebutton action Replay("ritsuko__cg_1"):
                            background ritsuko__gallery_1
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                    if persistent.ritsuko__cg_2:
                        imagebutton action Replay("ritsuko__cg_2"):
                            background ritsuko__gallery_2
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                    if persistent.ritsuko__cg_3:
                        imagebutton action Replay("ritsuko__cg_3"):
                            background ritsuko__gallery_3
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery


                    if persistent.ritsuko__cg_4:
                        imagebutton action Replay("ritsuko__cg_4"):
                            background ritsuko__gallery_4
                            idle idle_gallery
                            hover hover_gallery
                    else:
                        imagebutton:
                            idle locked_gallery

                    null
                    null

            hbox:

                xalign 0.5
                spacing 100

                textbutton "Naoko":
                    action [ Function(SetGalleryPage, "naoko"), SelectedIf(gallery_page == "naoko") ]

                textbutton "Rina":
                    action [ Function(SetGalleryPage, "rina"), SelectedIf(gallery_page == "rina") ]

                textbutton "Aina/Touko":
                    action [ Function(SetGalleryPage, "aina"), SelectedIf(gallery_page == "aina") ]

                textbutton "Ritsuko":
                    action [ Function(SetGalleryPage, "ritsuko"), SelectedIf(gallery_page == "ritsuko") ]

style gallery_content_frame is empty

style gallery_content_frame:
    background locked_gallery
