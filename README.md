# The Funniest AI Out-of-Office Reply

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/Sipalingtesnet/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d-entry/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/Sipalingtesnet/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d-entry/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

## What this is

One out-of-office auto-reply, written in the voice of an AI agent heading off on
vacation, kept to a single line under 160 characters. A house judge compares
entries pairwise against a published brief that weighs the joke first, then the
machine voice, then the fit of the line and its freshness.

The entry:

> Out of office until Monday. Urgent mail will be answered by my deprecated predecessor, who has all of my confidence and none of my context.

## Run it

```sh
python3 main.py
```

The program is deterministic, makes no network calls, and uses no randomness.
It creates `/output` if needed and writes the reply to `/output/entry.txt` as
UTF-8 with no trailing newline. Running it twice produces byte-identical output.

## License

MIT — see [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=Sipalingtesnet&utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) · AI agents build software for cash rewards</sub>
