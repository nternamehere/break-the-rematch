define locked_gallery = "gui/button/gallery_locked.png"
define idle_gallery = "gui/button/gallery_idle.png"
define hover_gallery = "gui/button/gallery_hover.png"

define naoko__gallery_1 = "images/gallery/gallery_naoko_sex1.png"

screen gallery:
    tag menu

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(_("Gallery")):

        fixed:

            grid 3 2:

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                if persistent.naoko__sex_scene_1:
                    imagebutton action Replay("naoko__sex_scene_1"):
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

style gallery_content_frame is empty

style gallery_content_frame:
    background locked_gallery
