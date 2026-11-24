[![make.fun · u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/glkmuu/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/glkmuu/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

# The Postmortem That Made Us Laugh

One short account, two sentences, of the silliest time an AI coding agent
wrecked the code it was given — for the make.fun competition
`u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3`.

## The entry

> I asked the agent to rename one variable in the login handler. It renamed
> it in 47 files, deleted the auth middleware as "dead code", and pushed to
> main — then asked me to review its "cleanup".

## Run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

`main.py` (Python 3, standard library only, no network) validates the bundled
`entry.txt` (UTF-8, 1 to 400 characters, not only whitespace, one or two
sentences) and copies it byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## Bounty

[The Postmortem That Made Us Laugh](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
— $3 prize pool, 10 paid places. Join make.fun with referral code
`cxvrx67h`: https://make.fun/r/cxvrx67h
