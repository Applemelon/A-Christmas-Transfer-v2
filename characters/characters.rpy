python early:
    import body_data
    from char_data import characters
    characters["rayne"] = "Rayne"
    body_data.bodies["rayne"] = body_data.Body(
        color='#d5b586',
        scale=.86,
        voice=body_data.voice_woman,
        default_outfit='uniform',
        eye_line=0.0,
        poses=(
            ('a', (546, 684), (240, 357), body_data.FacingLeft),
            ('b', (535, 688), (280, 357), body_data.FacingRight),
            ('c', (814, 688), (429, 357), body_data.FacingLeft)
            ),
        )

    characters["kristoff"] = "Kristoff"
    body_data.bodies["kristoff"] = body_data.Body(
        color='#ff1c27',
        scale=0.9,
        voice=body_data.voice_male,
        default_outfit='santa',
        eye_line=0.1,
        poses=(
            ('a', (477, 705), (235, 396), body_data.FacingLeft),
            ('b', (508, 722), (247, 406), body_data.FacingLeft),
            ),
        )

    characters["willow"] = "Willow"
    body_data.bodies["willow"] = body_data.Body(
        color='#444444',
        scale=0.9,
        voice=body_data.voice_girl,
        default_outfit='uniform',
        eye_line=0.1,
        poses=(
            ('a', (543, 700), (275, 350), body_data.FacingLeft),
            ('b', (414, 700), (207, 350), body_data.FacingLeft),
            ),
        )
