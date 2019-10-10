define locked_gallery = "gui/button/gallery_locked.png"
define idle_gallery = "gui/button/gallery_idle.png"
define hover_gallery = "gui/button/gallery_hover.png"

define special__gallery_2 = "images/gallery/gallery_rina_special_sex1.png"
define special__gallery_3 = "images/gallery/gallery_senji_sex1.png"
define special__gallery_4 = "images/gallery/gallery_touko_slut_sex1.png"
define special__gallery_5 = "images/gallery/gallery_touko_gyaru_sex1.png"

screen extra_scenes:
    tag menu
    
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(_("Extra Scenes")):

        fixed:

            grid 3 2:

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                if persistent.harem__cg_1:
                    imagebutton action Replay("rina_special_1"):
                        background special__gallery_2
                        idle idle_gallery
                        hover hover_gallery
                else:
                    imagebutton:
                        idle locked_gallery

                if persistent.harem__cg_1:
                    imagebutton action Replay("senji_special_1"):
                        background special__gallery_3
                        idle idle_gallery
                        hover hover_gallery
                else:
                    imagebutton:
                        idle locked_gallery


                if persistent.harem__cg_1:
                    imagebutton action Replay("touko_special_1"):
                        background special__gallery_4
                        idle idle_gallery
                        hover hover_gallery
                else:
                    imagebutton:
                        idle locked_gallery

                if persistent.harem__cg_1:
                    imagebutton action Replay("touko_special_2"):
                        background special__gallery_5
                        idle idle_gallery
                        hover hover_gallery
                else:
                    imagebutton:
                        idle locked_gallery
                null
                null

style gallery_content_frame is empty

style gallery_content_frame:
    background locked_gallery
