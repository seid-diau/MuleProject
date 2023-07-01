{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNHBpEfHbQ9PssxnjO7jfL1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/seid-diau/MuleProject/blob/main/loopandfunction.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uomONTMmgcjU",
        "outputId": "41cb081b-b0b2-49f0-fd28-5f1ee204e9cd"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "youtuber namediau said \n"
          ]
        }
      ],
      "source": [
        "youtuber = input(\"youtuber name\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"subscribe to \"+ youtuber)\n",
        "print(\"subscribe to {}\".format(youtuber))\n",
        "print(f\"subscrive to {youtuber}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2ZyvpEXTgkjy",
        "outputId": "4322bf63-92ab-4f03-8092-094be200d8dc"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "subscribe to diau said \n",
            "subscribe to diau said \n",
            "subscrive to diau said \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "adj = input(\"adjective:\")\n",
        "verb1 = input(\"verb: \")\n",
        "verb2 = input(\"verb: \")\n",
        "\n",
        "madlib=f\"computer programming is so {adj}! it imake me so excitred all the time because i love {verb1}. stay hydated and {verb2}\"\n",
        "print(madlib)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XSB8GpHNg3TR",
        "outputId": "cb845469-1c81-44e5-9dfb-d0434c679910"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "adjective:new \n",
            "verb: verb\n",
            "verb: verb\n",
            "computer programming is so new ! it imake me so excitred all the time because i love verb. stay hydated and verb\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "guess = input(\"guess the right number\")\n",
        "rand = random.randint(1,65)\n",
        "print(f\"your number is {guess} and the number is {rand}  \")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3NeV9MFlhq0a",
        "outputId": "67654fdb-c6d5-4203-8ca3-c200d778d533"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "guess the right number432\n",
            "your number is 432 and the number is 31  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#  guess game\n",
        "\n",
        "def guess(x):\n",
        "  rand= random.randint(1,x)\n",
        "  guess = 0\n",
        "  while guess !=rand:\n",
        "    guess = int(input(f\"Guess a number between 1 and {x}: \"))\n",
        "    if guess < rand:\n",
        "      print(\"Sorry too low . try again\")\n",
        "    elif guess > rand:\n",
        "      print(\"sorry too high try again \")\n",
        "    else:\n",
        "      print(f\"you won the number is {rand}\")\n",
        "\n",
        "guess(10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tyHPQZXTioC4",
        "outputId": "8389e66f-32b8-432c-d70e-38c8839535cb"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "guess a number between 1 and 10: 7\n",
            "sorry to high try again \n",
            "guess a number between 1 and 10: 6\n",
            "sorry to high try again \n",
            "guess a number between 1 and 10: 2\n",
            "Sorry to low . try again\n",
            "guess a number between 1 and 10: 4\n",
            "sorry to high try again \n",
            "guess a number between 1 and 10: 3\n",
            "you won the number is 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# computer guess our number\n",
        "\n",
        "def computerGuess(x):\n",
        "  low =1\n",
        "  high =x\n",
        "  feedback = \"\"\n",
        "  print(f\" you are guessing the number between {low} and {high}\")\n",
        "  while feedback != 'c':\n",
        "    if low != high :\n",
        "      guess = random.randint(low,high)\n",
        "    else:\n",
        "        guess = low\n",
        "    feedback = input(f\"is the {guess} too high (H),too low (L), or correct (C)\").lower()\n",
        "    if feedback ==\"h\":\n",
        "      high = guess -1\n",
        "    elif feedback =='l':\n",
        "      low = guess +1\n",
        "  print(f\"the computer guess our number {guess}. correctly\")\n",
        "computerGuess(1000)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 133
        },
        "id": "VKJykRcJjiD7",
        "outputId": "18808a02-75c4-47f2-dd0a-20e81545a7bb"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-35-e5b45fee7a14>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    computer guess our number\u001b[0m\n\u001b[0m             ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# rock paper scissor\n",
        "\n",
        "def is_win(player, opponent):\n",
        "\n",
        "  if(player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):\n",
        "    return  True\n",
        "\n",
        "\n",
        "\n",
        "def play() :\n",
        "\n",
        " user = input(\"what is choice ? 'r' for rock ,'p' for paper, 's' scissors\\n\")\n",
        " computer =random.choice(['r','p','s'])\n",
        " print(f\"user :{user} and computer : {computer}\")\n",
        " if user == computer :\n",
        "  print(\"it's a tie\")\n",
        "\n",
        " elif is_win(user, computer):\n",
        "    return(\"you win !\")\n",
        " else:\n",
        "\n",
        "  return( \"you lose !\")\n",
        "\n",
        "play()\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 90
        },
        "id": "YSykWA8Ysw-l",
        "outputId": "247f58d7-6f97-4cb4-a74c-014e22d4b274"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "what is choice ? 'r' for rock ,'p' for paper, 's' scissors\n",
            "s\n",
            "user :s and computer : r\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'you lose !'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# hangman game\n",
        "words = [\"aback\",\"abaft\",\"abandoned\",\"abashed\",\"aberrant\",\"abhorrent\",\"abiding\",\"abject\",\"ablaze\",\"able\",\"abnormal\",\"aboard\",\"aboriginal\",\"abortive\",\"abounding\",\"abrasive\",\"abrupt\",\"absent\",\"absorbed\",\"absorbing\",\"abstracted\",\"absurd\",\"abundant\",\"abusive\",\"acceptable\",\"accessible\",\"accidental\",\"accurate\",\"acid\",\"acidic\",\"acoustic\",\"acrid\",\"actually\",\"ad hoc\",\"adamant\",\"adaptable\",\"addicted\",\"adhesive\",\"adjoining\",\"adorable\",\"adventurous\",\"afraid\",\"aggressive\",\"agonizing\",\"agreeable\",\"ahead\",\"ajar\",\"alcoholic\",\"alert\",\"alike\",\"alive\",\"alleged\",\"alluring\",\"aloof\",\"amazing\",\"ambiguous\",\"ambitious\",\"amuck\",\"amused\",\"amusing\",\"ancient\",\"angry\",\"animated\",\"annoyed\",\"annoying\",\"anxious\",\"apathetic\",\"aquatic\",\"aromatic\",\"arrogant\",\"ashamed\",\"aspiring\",\"assorted\",\"astonishing\",\"attractive\",\"auspicious\",\"automatic\",\"available\",\"average\",\"awake\",\"aware\",\"awesome\",\"awful\",\"axiomatic\",\"bad\",\"barbarous\",\"bashful\",\"bawdy\",\"beautiful\",\"befitting\",\"belligerent\",\"beneficial\",\"bent\",\"berserk\",\"best\",\"better\",\"bewildered\",\"big\",\"billowy\",\"bite-sized\",\"bitter\",\"bizarre\",\"black\",\"black-and-white\",\"bloody\",\"blue\",\"blue-eyed\",\"blushing\",\"boiling\",\"boorish\",\"bored\",\"boring\",\"bouncy\",\"boundless\",\"brainy\",\"brash\",\"brave\",\"brawny\",\"breakable\",\"breezy\",\"brief\",\"bright\",\"bright\",\"broad\",\"broken\",\"brown\",\"bumpy\",\"burly\",\"bustling\",\"busy\",\"cagey\",\"calculating\",\"callous\",\"calm\",\"capable\",\"capricious\",\"careful\",\"careless\",\"caring\",\"cautious\",\"ceaseless\",\"certain\",\"changeable\",\"charming\",\"cheap\",\"cheerful\",\"chemical\",\"chief\",\"childlike\",\"chilly\",\"chivalrous\",\"chubby\",\"chunky\",\"clammy\",\"classy\",\"clean\",\"clear\",\"clever\",\"cloistered\",\"cloudy\",\"closed\",\"clumsy\",\"cluttered\",\"coherent\",\"cold\",\"colorful\",\"colossal\",\"combative\",\"comfortable\",\"common\",\"complete\",\"complex\",\"concerned\",\"condemned\",\"confused\",\"conscious\",\"cooing\",\"cool\",\"cooperative\",\"coordinated\",\"courageous\",\"cowardly\",\"crabby\",\"craven\",\"crazy\",\"creepy\",\"crooked\",\"crowded\",\"cruel\",\"cuddly\",\"cultured\",\"cumbersome\",\"curious\",\"curly\",\"curved\",\"curvy\",\"cut\",\"cute\",\"cute\",\"cynical\",\"daffy\",\"daily\",\"damaged\",\"damaging\",\"damp\",\"dangerous\",\"dapper\",\"dark\",\"dashing\",\"dazzling\",\"dead\",\"deadpan\",\"deafening\",\"dear\",\"debonair\",\"decisive\",\"decorous\",\"deep\",\"deeply\",\"defeated\",\"defective\",\"defiant\",\"delicate\",\"delicious\",\"delightful\",\"demonic\",\"delirious\",\"dependent\",\"depressed\",\"deranged\",\"descriptive\",\"deserted\",\"detailed\",\"determined\",\"devilish\",\"didactic\",\"different\",\"difficult\",\"diligent\",\"direful\",\"dirty\",\"disagreeable\",\"disastrous\",\"discreet\",\"disgusted\",\"disgusting\",\"disillusioned\",\"dispensable\",\"distinct\",\"disturbed\",\"divergent\",\"dizzy\",\"domineering\",\"doubtful\",\"drab\",\"draconian\",\"dramatic\",\"dreary\",\"drunk\",\"dry\",\"dull\",\"dusty\",\"dusty\",\"dynamic\",\"dysfunctional\",\"eager\",\"early\",\"earsplitting\",\"earthy\",\"easy\",\"eatable\",\"economic\",\"educated\",\"efficacious\",\"efficient\",\"eight\",\"elastic\",\"elated\",\"elderly\",\"electric\",\"elegant\",\"elfin\",\"elite\",\"embarrassed\",\"eminent\",\"empty\",\"enchanted\",\"enchanting\",\"encouraging\",\"endurable\",\"energetic\",\"enormous\",\"entertaining\",\"enthusiastic\",\"envious\",\"equable\",\"equal\",\"erect\",\"erratic\",\"ethereal\",\"evanescent\",\"evasive\",\"even\",\"excellent\",\"excited\",\"exciting\",\"exclusive\",\"exotic\",\"expensive\",\"extra-large\",\"extra-small\",\"exuberant\",\"exultant\",\"fabulous\",\"faded\",\"faint\",\"fair\",\"faithful\",\"fallacious\",\"false\",\"familiar\",\"famous\",\"fanatical\",\"fancy\",\"fantastic\",\"far\",\"far-flung\",\"fascinated\",\"fast\",\"fat\",\"faulty\",\"fearful\",\"fearless\",\"feeble\",\"feigned\",\"female\",\"fertile\",\"festive\",\"few\",\"fierce\",\"filthy\",\"fine\",\"finicky\",\"first\",\"five\",\"fixed\",\"flagrant\",\"flaky\",\"flashy\",\"flat\",\"flawless\",\"flimsy\",\"flippant\",\"flowery\",\"fluffy\",\"fluttering\",\"foamy\",\"foolish\",\"foregoing\",\"forgetful\",\"fortunate\",\"four\",\"frail\",\"fragile\",\"frantic\",\"free\",\"freezing\",\"frequent\",\"fresh\",\"fretful\",\"friendly\",\"frightened\",\"frightening\",\"full\",\"fumbling\",\"functional\",\"funny\",\"furry\",\"furtive\",\"future\",\"futuristic\",\"fuzzy\",\"gabby\",\"gainful\",\"gamy\",\"gaping\",\"garrulous\",\"gaudy\",\"general\",\"gentle\",\"giant\",\"giddy\",\"gifted\",\"gigantic\",\"glamorous\",\"gleaming\",\"glib\",\"glistening\",\"glorious\",\"glossy\",\"godly\",\"good\",\"goofy\",\"gorgeous\",\"graceful\",\"grandiose\",\"grateful\",\"gratis\",\"gray\",\"greasy\",\"great\",\"greedy\",\"green\",\"grey\",\"grieving\",\"groovy\",\"grotesque\",\"grouchy\",\"grubby\",\"gruesome\",\"grumpy\",\"guarded\",\"guiltless\",\"gullible\",\"gusty\",\"guttural\",\"habitual\",\"half\",\"hallowed\",\"halting\",\"handsome\",\"handsomely\",\"handy\",\"hanging\",\"hapless\",\"happy\",\"hard\",\"hard-to-find\",\"harmonious\",\"harsh\",\"hateful\",\"heady\",\"healthy\",\"heartbreaking\",\"heavenly\",\"heavy\",\"hellish\",\"helpful\",\"helpless\",\"hesitant\",\"hideous\",\"high\",\"highfalutin\",\"high-pitched\",\"hilarious\",\"hissing\",\"historical\",\"holistic\",\"hollow\",\"homeless\",\"homely\",\"honorable\",\"horrible\",\"hospitable\",\"hot\",\"huge\",\"hulking\",\"humdrum\",\"humorous\",\"hungry\",\"hurried\",\"hurt\",\"hushed\",\"husky\",\"hypnotic\",\"hysterical\",\"icky\",\"icy\",\"idiotic\",\"ignorant\",\"ill\",\"illegal\",\"ill-fated\",\"ill-informed\",\"illustrious\",\"imaginary\",\"immense\",\"imminent\",\"impartial\",\"imperfect\",\"impolite\",\"important\",\"imported\",\"impossible\",\"incandescent\",\"incompetent\",\"inconclusive\",\"industrious\",\"incredible\",\"inexpensive\",\"infamous\",\"innate\",\"innocent\",\"inquisitive\",\"insidious\",\"instinctive\",\"intelligent\",\"interesting\",\"internal\",\"invincible\",\"irate\",\"irritating\",\"itchy\",\"jaded\",\"jagged\",\"jazzy\",\"jealous\",\"jittery\",\"jobless\",\"jolly\",\"joyous\",\"judicious\",\"juicy\",\"jumbled\",\"jumpy\",\"juvenile\",\"kaput\",\"keen\",\"kind\",\"kindhearted\",\"kindly\",\"knotty\",\"knowing\",\"knowledgeable\",\"known\",\"labored\",\"lackadaisical\",\"lacking\",\"lame\",\"lamentable\",\"languid\",\"large\",\"last\",\"late\",\"laughable\",\"lavish\",\"lazy\",\"lean\",\"learned\",\"left\",\"legal\",\"lethal\",\"level\",\"lewd\",\"light\",\"like\",\"likeable\",\"limping\",\"literate\",\"little\",\"lively\",\"lively\",\"living\",\"lonely\",\"long\",\"longing\",\"long-term\",\"loose\",\"lopsided\",\"loud\",\"loutish\",\"lovely\",\"loving\",\"low\",\"lowly\",\"lucky\",\"ludicrous\",\"lumpy\",\"lush\",\"luxuriant\",\"lying\",\"lyrical\",\"macabre\",\"macho\",\"maddening\",\"madly\",\"magenta\",\"magical\",\"magnificent\",\"majestic\",\"makeshift\",\"male\",\"malicious\",\"mammoth\",\"maniacal\",\"many\",\"marked\",\"massive\",\"married\",\"marvelous\",\"material\",\"materialistic\",\"mature\",\"mean\",\"measly\",\"meaty\",\"medical\",\"meek\",\"mellow\",\"melodic\",\"melted\",\"merciful\",\"mere\",\"messy\",\"mighty\",\"military\",\"milky\",\"mindless\",\"miniature\",\"minor\",\"miscreant\",\"misty\",\"mixed\",\"moaning\",\"modern\",\"moldy\",\"momentous\",\"motionless\",\"mountainous\",\"muddled\",\"mundane\",\"murky\",\"mushy\",\"mute\",\"mysterious\",\"naive\",\"nappy\",\"narrow\",\"nasty\",\"natural\",\"naughty\",\"nauseating\",\"near\",\"neat\",\"nebulous\",\"necessary\",\"needless\",\"needy\",\"neighborly\",\"nervous\",\"new\",\"next\",\"nice\",\"nifty\",\"nimble\",\"nine\",\"nippy\",\"noiseless\",\"noisy\",\"nonchalant\",\"nondescript\",\"nonstop\",\"normal\",\"nostalgic\",\"nosy\",\"noxious\",\"null\",\"numberless\",\"numerous\",\"nutritious\",\"nutty\",\"oafish\",\"obedient\",\"obeisant\",\"obese\",\"obnoxious\",\"obscene\",\"obsequious\",\"observant\",\"obsolete\",\"obtainable\",\"oceanic\",\"odd\",\"offbeat\",\"old\",\"old-fashioned\",\"omniscient\",\"one\",\"onerous\",\"open\",\"opposite\",\"optimal\",\"orange\",\"ordinary\",\"organic\",\"ossified\",\"outgoing\",\"outrageous\",\"outstanding\",\"oval\",\"overconfident\",\"overjoyed\",\"overrated\",\"overt\",\"overwrought\",\"painful\",\"painstaking\",\"pale\",\"paltry\",\"panicky\",\"panoramic\",\"parallel\",\"parched\",\"parsimonious\",\"past\",\"pastoral\",\"pathetic\",\"peaceful\",\"penitent\",\"perfect\",\"periodic\",\"permissible\",\"perpetual\",\"petite\",\"petite\",\"phobic\",\"physical\",\"picayune\",\"pink\",\"piquant\",\"placid\",\"plain\",\"plant\",\"plastic\",\"plausible\",\"pleasant\",\"plucky\",\"pointless\",\"poised\",\"polite\",\"political\",\"poor\",\"possessive\",\"possible\",\"powerful\",\"precious\",\"premium\",\"present\",\"pretty\",\"previous\",\"pricey\",\"prickly\",\"private\",\"probable\",\"productive\",\"profuse\",\"protective\",\"proud\",\"psychedelic\",\"psychotic\",\"public\",\"puffy\",\"pumped\",\"puny\",\"purple\",\"purring\",\"pushy\",\"puzzled\",\"puzzling\",\"quack\",\"quaint\",\"quarrelsome\",\"questionable\",\"quick\",\"quickest\",\"quiet\",\"quirky\",\"quixotic\",\"quizzical\",\"rabid\",\"racial\",\"ragged\",\"rainy\",\"rambunctious\",\"rampant\",\"rapid\",\"rare\",\"raspy\",\"ratty\",\"ready\",\"real\",\"rebel\",\"receptive\",\"recondite\",\"red\",\"redundant\",\"reflective\",\"regular\",\"relieved\",\"remarkable\",\"reminiscent\",\"repulsive\",\"resolute\",\"resonant\",\"responsible\",\"rhetorical\",\"rich\",\"right\",\"righteous\",\"rightful\",\"rigid\",\"ripe\",\"ritzy\",\"roasted\",\"robust\",\"romantic\",\"roomy\",\"rotten\",\"rough\",\"round\",\"royal\",\"ruddy\",\"rude\",\"rural\",\"rustic\",\"ruthless\",\"sable\",\"sad\",\"safe\",\"salty\",\"same\",\"sassy\",\"satisfying\",\"savory\",\"scandalous\",\"scarce\",\"scared\",\"scary\",\"scattered\",\"scientific\",\"scintillating\",\"scrawny\",\"screeching\",\"second\",\"second-hand\",\"secret\",\"secretive\",\"sedate\",\"seemly\",\"selective\",\"selfish\",\"separate\",\"serious\",\"shaggy\",\"shaky\",\"shallow\",\"sharp\",\"shiny\",\"shivering\",\"shocking\",\"short\",\"shrill\",\"shut\",\"shy\",\"sick\",\"silent\",\"silent\",\"silky\",\"silly\",\"simple\",\"simplistic\",\"sincere\",\"six\",\"skillful\",\"skinny\",\"sleepy\",\"slim\",\"slimy\",\"slippery\",\"sloppy\",\"slow\",\"small\",\"smart\",\"smelly\",\"smiling\",\"smoggy\",\"smooth\",\"sneaky\",\"snobbish\",\"snotty\",\"soft\",\"soggy\",\"solid\",\"somber\",\"sophisticated\",\"sordid\",\"sore\",\"sore\",\"sour\",\"sparkling\",\"special\",\"spectacular\",\"spicy\",\"spiffy\",\"spiky\",\"spiritual\",\"spiteful\",\"splendid\",\"spooky\",\"spotless\",\"spotted\",\"spotty\",\"spurious\",\"squalid\",\"square\",\"squealing\",\"squeamish\",\"staking\",\"stale\",\"standing\",\"statuesque\",\"steadfast\",\"steady\",\"steep\",\"stereotyped\",\"sticky\",\"stiff\",\"stimulating\",\"stingy\",\"stormy\",\"straight\",\"strange\",\"striped\",\"strong\",\"stupendous\",\"stupid\",\"sturdy\",\"subdued\",\"subsequent\",\"substantial\",\"successful\",\"succinct\",\"sudden\",\"sulky\",\"super\",\"superb\",\"superficial\",\"supreme\",\"swanky\",\"sweet\",\"sweltering\",\"swift\",\"symptomatic\",\"synonymous\",\"taboo\",\"tacit\",\"tacky\",\"talented\",\"tall\",\"tame\",\"tan\",\"tangible\",\"tangy\",\"tart\",\"tasteful\",\"tasteless\",\"tasty\",\"tawdry\",\"tearful\",\"tedious\",\"teeny\",\"teeny-tiny\",\"telling\",\"temporary\",\"ten\",\"tender\",\"tense\",\"tense\",\"tenuous\",\"terrible\",\"terrific\",\"tested\",\"testy\",\"thankful\",\"therapeutic\",\"thick\",\"thin\",\"thinkable\",\"third\",\"thirsty\",\"thirsty\",\"thoughtful\",\"thoughtless\",\"threatening\",\"three\",\"thundering\",\"tidy\",\"tight\",\"tightfisted\",\"tiny\",\"tired\",\"tiresome\",\"toothsome\",\"torpid\",\"tough\",\"towering\",\"tranquil\",\"trashy\",\"tremendous\",\"tricky\",\"trite\",\"troubled\",\"truculent\",\"true\",\"truthful\",\"two\",\"typical\",\"ubiquitous\",\"ugliest\",\"ugly\",\"ultra\",\"unable\",\"unaccountable\",\"unadvised\",\"unarmed\",\"unbecoming\",\"unbiased\",\"uncovered\",\"understood\",\"undesirable\",\"unequal\",\"unequaled\",\"uneven\",\"unhealthy\",\"uninterested\",\"unique\",\"unkempt\",\"unknown\",\"unnatural\",\"unruly\",\"unsightly\",\"unsuitable\",\"untidy\",\"unused\",\"unusual\",\"unwieldy\",\"unwritten\",\"upbeat\",\"uppity\",\"upset\",\"uptight\",\"used\",\"useful\",\"useless\",\"utopian\",\"utter\",\"uttermost\",\"vacuous\",\"vagabond\",\"vague\",\"valuable\",\"various\",\"vast\",\"vengeful\",\"venomous\",\"verdant\",\"versed\",\"victorious\",\"vigorous\",\"violent\",\"violet\",\"vivacious\",\"voiceless\",\"volatile\",\"voracious\",\"vulgar\",\"wacky\",\"waggish\",\"waiting\",\"wakeful\",\"wandering\",\"wanting\",\"warlike\",\"warm\",\"wary\",\"wasteful\",\"watery\",\"weak\",\"wealthy\",\"weary\",\"well-groomed\",\"well-made\",\"well-off\",\"well-to-do\",\"wet\",\"whimsical\",\"whispering\",\"white\",\"whole\",\"wholesale\",\"wicked\",\"wide\",\"wide-eyed\",\"wiggly\",\"wild\",\"willing\",\"windy\",\"wiry\",\"wise\",\"wistful\",\"witty\",\"woebegone\",\"womanly\",\"wonderful\",\"wooden\",\"woozy\",\"workable\",\"worried\",\"worthless\",\"wrathful\",\"wretched\",\"wrong\",\"wry\",\"yellow\",\"yielding\",\"young\",\"youthful\",\"yummy\",\"zany\",\"zealous\",\"zesty\",\"zippy\",\"zonked\",\"account\",\"achiever\",\"acoustics\",\"act\",\"action\",\"activity\",\"actor\",\"addition\",\"adjustment\",\"advertisement\",\"advice\",\"aftermath\",\"afternoon\",\"afterthought\",\"agreement\",\"air\",\"airplane\",\"airport\",\"alarm\",\"amount\",\"amusement\",\"anger\",\"angle\",\"animal\",\"ants\",\"apparatus\",\"apparel\",\"appliance\",\"approval\",\"arch\",\"argument\",\"arithmetic\",\"arm\",\"army\",\"art\",\"attack\",\"attraction\",\"aunt\",\"authority\",\"babies\",\"baby\",\"back\",\"badge\",\"bag\",\"bait\",\"balance\",\"ball\",\"base\",\"baseball\",\"basin\",\"basket\",\"basketball\",\"bat\",\"bath\",\"battle\",\"bead\",\"bear\",\"bed\",\"bedroom\",\"beds\",\"bee\",\"beef\",\"beginner\",\"behavior\",\"belief\",\"believe\",\"bell\",\"bells\",\"berry\",\"bike\",\"bikes\",\"bird\",\"birds\",\"birth\",\"birthday\",\"bit\",\"bite\",\"blade\",\"blood\",\"blow\",\"board\",\"boat\",\"bomb\",\"bone\",\"book\",\"books\",\"boot\",\"border\",\"bottle\",\"boundary\",\"box\",\"boy\",\"brake\",\"branch\",\"brass\",\"breath\",\"brick\",\"bridge\",\"brother\",\"bubble\",\"bucket\",\"building\",\"bulb\",\"burst\",\"bushes\",\"business\",\"butter\",\"button\",\"cabbage\",\"cable\",\"cactus\",\"cake\",\"cakes\",\"calculator\",\"calendar\",\"camera\",\"camp\",\"can\",\"cannon\",\"canvas\",\"cap\",\"caption\",\"car\",\"card\",\"care\",\"carpenter\",\"carriage\",\"cars\",\"cart\",\"cast\",\"cat\",\"cats\",\"cattle\",\"cause\",\"cave\",\"celery\",\"cellar\",\"cemetery\",\"cent\",\"chalk\",\"chance\",\"change\",\"channel\",\"cheese\",\"cherries\",\"cherry\",\"chess\",\"chicken\",\"chickens\",\"children\",\"chin\",\"church\",\"circle\",\"clam\",\"class\",\"cloth\",\"clover\",\"club\",\"coach\",\"coal\",\"coast\",\"coat\",\"cobweb\",\"coil\",\"collar\",\"color\",\"committee\",\"company\",\"comparison\",\"competition\",\"condition\",\"connection\",\"control\",\"cook\",\"copper\",\"corn\",\"cough\",\"country\",\"cover\",\"cow\",\"cows\",\"crack\",\"cracker\",\"crate\",\"crayon\",\"cream\",\"creator\",\"creature\",\"credit\",\"crib\",\"crime\",\"crook\",\"crow\",\"crowd\",\"crown\",\"cub\",\"cup\",\"current\",\"curtain\",\"curve\",\"cushion\",\"dad\",\"daughter\",\"day\",\"death\",\"debt\",\"decision\",\"deer\",\"degree\",\"design\",\"desire\",\"desk\",\"destruction\",\"detail\",\"development\",\"digestion\",\"dime\",\"dinner\",\"dinosaurs\",\"direction\",\"dirt\",\"discovery\",\"discussion\",\"distance\",\"distribution\",\"division\",\"dock\",\"doctor\",\"dog\",\"dogs\",\"doll\",\"dolls\",\"donkey\",\"door\",\"downtown\",\"drain\",\"drawer\",\"dress\",\"drink\",\"driving\",\"drop\",\"duck\",\"ducks\",\"dust\",\"ear\",\"earth\",\"earthquake\",\"edge\",\"education\",\"effect\",\"egg\",\"eggnog\",\"eggs\",\"elbow\",\"end\",\"engine\",\"error\",\"event\",\"example\",\"exchange\",\"existence\",\"expansion\",\"experience\",\"expert\",\"eye\",\"eyes\",\"face\",\"fact\",\"fairies\",\"fall\",\"fang\",\"farm\",\"fear\",\"feeling\",\"field\",\"finger\",\"finger\",\"fire\",\"fireman\",\"fish\",\"flag\",\"flame\",\"flavor\",\"flesh\",\"flight\",\"flock\",\"floor\",\"flower\",\"flowers\",\"fly\",\"fog\",\"fold\",\"food\",\"foot\",\"force\",\"fork\",\"form\",\"fowl\",\"frame\",\"friction\",\"friend\",\"friends\",\"frog\",\"frogs\",\"front\",\"fruit\",\"fuel\",\"furniture\",\"gate\",\"geese\",\"ghost\",\"giants\",\"giraffe\",\"girl\",\"girls\",\"glass\",\"glove\",\"gold\",\"government\",\"governor\",\"grade\",\"grain\",\"grandfather\",\"grandmother\",\"grape\",\"grass\",\"grip\",\"ground\",\"group\",\"growth\",\"guide\",\"guitar\",\"gun\",\"hair\",\"haircut\",\"hall\",\"hammer\",\"hand\",\"hands\",\"harbor\",\"harmony\",\"hat\",\"hate\",\"head\",\"health\",\"heat\",\"hill\",\"history\",\"hobbies\",\"hole\",\"holiday\",\"home\",\"honey\",\"hook\",\"hope\",\"horn\",\"horse\",\"horses\",\"hose\",\"hospital\",\"hot\",\"hour\",\"house\",\"houses\",\"humor\",\"hydrant\",\"ice\",\"icicle\",\"idea\",\"impulse\",\"income\",\"increase\",\"industry\",\"ink\",\"insect\",\"instrument\",\"insurance\",\"interest\",\"invention\",\"iron\",\"island\",\"jail\",\"jam\",\"jar\",\"jeans\",\"jelly\",\"jellyfish\",\"jewel\",\"join\",\"judge\",\"juice\",\"jump\",\"kettle\",\"key\",\"kick\",\"kiss\",\"kittens\",\"kitty\",\"knee\",\"knife\",\"knot\",\"knowledge\",\"laborer\",\"lace\",\"ladybug\",\"lake\",\"lamp\",\"land\",\"language\",\"laugh\",\"leather\",\"leg\",\"legs\",\"letter\",\"letters\",\"lettuce\",\"level\",\"library\",\"limit\",\"line\",\"linen\",\"lip\",\"liquid\",\"loaf\",\"lock\",\"locket\",\"look\",\"loss\",\"love\",\"low\",\"lumber\",\"lunch\",\"lunchroom\",\"machine\",\"magic\",\"maid\",\"mailbox\",\"man\",\"marble\",\"mark\",\"market\",\"mask\",\"mass\",\"match\",\"meal\",\"measure\",\"meat\",\"meeting\",\"memory\",\"men\",\"metal\",\"mice\",\"middle\",\"milk\",\"mind\",\"mine\",\"minister\",\"mint\",\"minute\",\"mist\",\"mitten\",\"mom\",\"money\",\"monkey\",\"month\",\"moon\",\"morning\",\"mother\",\"motion\",\"mountain\",\"mouth\",\"move\",\"muscle\",\"name\",\"nation\",\"neck\",\"need\",\"needle\",\"nerve\",\"nest\",\"night\",\"noise\",\"north\",\"nose\",\"note\",\"notebook\",\"number\",\"nut\",\"oatmeal\",\"observation\",\"ocean\",\"offer\",\"office\",\"oil\",\"orange\",\"oranges\",\"order\",\"oven\",\"page\",\"pail\",\"pan\",\"pancake\",\"paper\",\"parcel\",\"part\",\"partner\",\"party\",\"passenger\",\"payment\",\"peace\",\"pear\",\"pen\",\"pencil\",\"person\",\"pest\",\"pet\",\"pets\",\"pickle\",\"picture\",\"pie\",\"pies\",\"pig\",\"pigs\",\"pin\",\"pipe\",\"pizzas\",\"place\",\"plane\",\"planes\",\"plant\",\"plantation\",\"plants\",\"plastic\",\"plate\",\"play\",\"playground\",\"pleasure\",\"plot\",\"plough\",\"pocket\",\"point\",\"poison\",\"pollution\",\"popcorn\",\"porter\",\"position\",\"pot\",\"potato\",\"powder\",\"power\",\"price\",\"produce\",\"profit\",\"property\",\"prose\",\"protest\",\"pull\",\"pump\",\"punishment\",\"purpose\",\"push\",\"quarter\",\"quartz\",\"queen\",\"question\",\"quicksand\",\"quiet\",\"quill\",\"quilt\",\"quince\",\"quiver\",\"rabbit\",\"rabbits\",\"rail\",\"railway\",\"rain\",\"rainstorm\",\"rake\",\"range\",\"rat\",\"rate\",\"ray\",\"reaction\",\"reading\",\"reason\",\"receipt\",\"recess\",\"record\",\"regret\",\"relation\",\"religion\",\"representative\",\"request\",\"respect\",\"rest\",\"reward\",\"rhythm\",\"rice\",\"riddle\",\"rifle\",\"ring\",\"rings\",\"river\",\"road\",\"robin\",\"rock\",\"rod\",\"roll\",\"roof\",\"room\",\"root\",\"rose\",\"route\",\"rub\",\"rule\",\"run\",\"sack\",\"sail\",\"salt\",\"sand\",\"scale\",\"scarecrow\",\"scarf\",\"scene\",\"scent\",\"school\",\"science\",\"scissors\",\"screw\",\"sea\",\"seashore\",\"seat\",\"secretary\",\"seed\",\"selection\",\"self\",\"sense\",\"servant\",\"shade\",\"shake\",\"shame\",\"shape\",\"sheep\",\"sheet\",\"shelf\",\"ship\",\"shirt\",\"shock\",\"shoe\",\"shoes\",\"shop\",\"show\",\"side\",\"sidewalk\",\"sign\",\"silk\",\"silver\",\"sink\",\"sister\",\"sisters\",\"size\",\"skate\",\"skin\",\"skirt\",\"sky\",\"slave\",\"sleep\",\"sleet\",\"slip\",\"slope\",\"smash\",\"smell\",\"smile\",\"smoke\",\"snail\",\"snails\",\"snake\",\"snakes\",\"sneeze\",\"snow\",\"soap\",\"society\",\"sock\",\"soda\",\"sofa\",\"son\",\"song\",\"songs\",\"sort\",\"sound\",\"soup\",\"space\",\"spade\",\"spark\",\"spiders\",\"sponge\",\"spoon\",\"spot\",\"spring\",\"spy\",\"square\",\"squirrel\",\"stage\",\"stamp\",\"star\",\"start\",\"statement\",\"station\",\"steam\",\"steel\",\"stem\",\"step\",\"stew\",\"stick\",\"sticks\",\"stitch\",\"stocking\",\"stomach\",\"stone\",\"stop\",\"store\",\"story\",\"stove\",\"stranger\",\"straw\",\"stream\",\"street\",\"stretch\",\"string\",\"structure\",\"substance\",\"sugar\",\"suggestion\",\"suit\",\"summer\",\"sun\",\"support\",\"surprise\",\"sweater\",\"swim\",\"swing\",\"system\",\"table\",\"tail\",\"talk\",\"tank\",\"taste\",\"tax\",\"teaching\",\"team\",\"teeth\",\"temper\",\"tendency\",\"tent\",\"territory\",\"test\",\"texture\",\"theory\",\"thing\",\"things\",\"thought\",\"thread\",\"thrill\",\"throat\",\"throne\",\"thumb\",\"thunder\",\"ticket\",\"tiger\",\"time\",\"tin\",\"title\",\"toad\",\"toe\",\"toes\",\"tomatoes\",\"tongue\",\"tooth\",\"toothbrush\",\"toothpaste\",\"top\",\"touch\",\"town\",\"toy\",\"toys\",\"trade\",\"trail\",\"train\",\"trains\",\"tramp\",\"transport\",\"tray\",\"treatment\",\"tree\",\"trees\",\"trick\",\"trip\",\"trouble\",\"trousers\",\"truck\",\"trucks\",\"tub\",\"turkey\",\"turn\",\"twig\",\"twist\",\"umbrella\",\"uncle\",\"underwear\",\"unit\",\"use\",\"vacation\",\"value\",\"van\",\"vase\",\"vegetable\",\"veil\",\"vein\",\"verse\",\"vessel\",\"vest\",\"view\",\"visitor\",\"voice\",\"volcano\",\"volleyball\",\"voyage\",\"walk\",\"wall\",\"war\",\"wash\",\"waste\",\"watch\",\"water\",\"wave\",\"waves\",\"wax\",\"way\",\"wealth\",\"weather\",\"week\",\"weight\",\"wheel\",\"whip\",\"whistle\",\"wilderness\",\"wind\",\"window\",\"wine\",\"wing\",\"winter\",\"wire\",\"wish\",\"woman\",\"women\",\"wood\",\"wool\",\"word\",\"work\",\"worm\",\"wound\",\"wren\",\"wrench\",\"wrist\",\"writer\",\"writing\",\"yak\",\"yam\",\"yard\",\"yarn\",\"year\",\"yoke\",\"zebra\",\"zephyr\",\"zinc\",\"zipper\",\"zoo\",\"accept\",\"add\",\"admire\",\"admit\",\"advise\",\"afford\",\"agree\",\"alert\",\"allow\",\"amuse\",\"analyse\",\"announce\",\"annoy\",\"answer\",\"apologise\",\"appear\",\"applaud\",\"appreciate\",\"approve\",\"argue\",\"arrange\",\"arrest\",\"arrive\",\"ask\",\"attach\",\"attack\",\"attempt\",\"attend\",\"attract\",\"avoid\",\"back\",\"bake\",\"balance\",\"ban\",\"bang\",\"bare\",\"bat\",\"bathe\",\"battle\",\"beam\",\"beg\",\"behave\",\"belong\",\"bleach\",\"bless\",\"blind\",\"blink\",\"blot\",\"blush\",\"boast\",\"boil\",\"bolt\",\"bomb\",\"book\",\"bore\",\"borrow\",\"bounce\",\"bow\",\"box\",\"brake\",\"branch\",\"breathe\",\"bruise\",\"brush\",\"bubble\",\"bump\",\"burn\",\"bury\",\"buzz\",\"calculate\",\"call\",\"camp\",\"care\",\"carry\",\"carve\",\"cause\",\"challenge\",\"change\",\"charge\",\"chase\",\"cheat\",\"check\",\"cheer\",\"chew\",\"choke\",\"chop\",\"claim\",\"clap\",\"clean\",\"clear\",\"clip\",\"close\",\"coach\",\"coil\",\"collect\",\"colour\",\"comb\",\"command\",\"communicate\",\"compare\",\"compete\",\"complain\",\"complete\",\"concentrate\",\"concern\",\"confess\",\"confuse\",\"connect\",\"consider\",\"consist\",\"contain\",\"continue\",\"copy\",\"correct\",\"cough\",\"count\",\"cover\",\"crack\",\"crash\",\"crawl\",\"cross\",\"crush\",\"cry\",\"cure\",\"curl\",\"curve\",\"cycle\",\"dam\",\"damage\",\"dance\",\"dare\",\"decay\",\"deceive\",\"decide\",\"decorate\",\"delay\",\"delight\",\"deliver\",\"depend\",\"describe\",\"desert\",\"deserve\",\"destroy\",\"detect\",\"develop\",\"disagree\",\"disappear\",\"disapprove\",\"disarm\",\"discover\",\"dislike\",\"divide\",\"double\",\"doubt\",\"drag\",\"drain\",\"dream\",\"dress\",\"drip\",\"drop\",\"drown\",\"drum\",\"dry\",\"dust\",\"earn\",\"educate\",\"embarrass\",\"employ\",\"empty\",\"encourage\",\"end\",\"enjoy\",\"enter\",\"entertain\",\"escape\",\"examine\",\"excite\",\"excuse\",\"exercise\",\"exist\",\"expand\",\"expect\",\"explain\",\"explode\",\"extend\",\"face\",\"fade\",\"fail\",\"fancy\",\"fasten\",\"fax\",\"fear\",\"fence\",\"fetch\",\"file\",\"fill\",\"film\",\"fire\",\"fit\",\"fix\",\"flap\",\"flash\",\"float\",\"flood\",\"flow\",\"flower\",\"fold\",\"follow\",\"fool\",\"force\",\"form\",\"found\",\"frame\",\"frighten\",\"fry\",\"gather\",\"gaze\",\"glow\",\"glue\",\"grab\",\"grate\",\"grease\",\"greet\",\"grin\",\"grip\",\"groan\",\"guarantee\",\"guard\",\"guess\",\"guide\",\"hammer\",\"hand\",\"handle\",\"hang\",\"happen\",\"harass\",\"harm\",\"hate\",\"haunt\",\"head\",\"heal\",\"heap\",\"heat\",\"help\",\"hook\",\"hop\",\"hope\",\"hover\",\"hug\",\"hum\",\"hunt\",\"hurry\",\"identify\",\"ignore\",\"imagine\",\"impress\",\"improve\",\"include\",\"increase\",\"influence\",\"inform\",\"inject\",\"injure\",\"instruct\",\"intend\",\"interest\",\"interfere\",\"interrupt\",\"introduce\",\"invent\",\"invite\",\"irritate\",\"itch\",\"jail\",\"jam\",\"jog\",\"join\",\"joke\",\"judge\",\"juggle\",\"jump\",\"kick\",\"kill\",\"kiss\",\"kneel\",\"knit\",\"knock\",\"knot\",\"label\",\"land\",\"last\",\"laugh\",\"launch\",\"learn\",\"level\",\"license\",\"lick\",\"lie\",\"lighten\",\"like\",\"list\",\"listen\",\"live\",\"load\",\"lock\",\"long\",\"look\",\"love\",\"man\",\"manage\",\"march\",\"mark\",\"marry\",\"match\",\"mate\",\"matter\",\"measure\",\"meddle\",\"melt\",\"memorise\",\"mend\",\"mess up\",\"milk\",\"mine\",\"miss\",\"mix\",\"moan\",\"moor\",\"mourn\",\"move\",\"muddle\",\"mug\",\"multiply\",\"murder\",\"nail\",\"name\",\"need\",\"nest\",\"nod\",\"note\",\"notice\",\"number\",\"obey\",\"object\",\"observe\",\"obtain\",\"occur\",\"offend\",\"offer\",\"open\",\"order\",\"overflow\",\"owe\",\"own\",\"pack\",\"paddle\",\"paint\",\"park\",\"part\",\"pass\",\"paste\",\"pat\",\"pause\",\"peck\",\"pedal\",\"peel\",\"peep\",\"perform\",\"permit\",\"phone\",\"pick\",\"pinch\",\"pine\",\"place\",\"plan\",\"plant\",\"play\",\"please\",\"plug\",\"point\",\"poke\",\"polish\",\"pop\",\"possess\",\"post\",\"pour\",\"practise\",\"pray\",\"preach\",\"precede\",\"prefer\",\"prepare\",\"present\",\"preserve\",\"press\",\"pretend\",\"prevent\",\"prick\",\"print\",\"produce\",\"program\",\"promise\",\"protect\",\"provide\",\"pull\",\"pump\",\"punch\",\"puncture\",\"punish\",\"push\",\"question\",\"queue\",\"race\",\"radiate\",\"rain\",\"raise\",\"reach\",\"realise\",\"receive\",\"recognise\",\"record\",\"reduce\",\"reflect\",\"refuse\",\"regret\",\"reign\",\"reject\",\"rejoice\",\"relax\",\"release\",\"rely\",\"remain\",\"remember\",\"remind\",\"remove\",\"repair\",\"repeat\",\"replace\",\"reply\",\"report\",\"reproduce\",\"request\",\"rescue\",\"retire\",\"return\",\"rhyme\",\"rinse\",\"risk\",\"rob\",\"rock\",\"roll\",\"rot\",\"rub\",\"ruin\",\"rule\",\"rush\",\"sack\",\"sail\",\"satisfy\",\"save\",\"saw\",\"scare\",\"scatter\",\"scold\",\"scorch\",\"scrape\",\"scratch\",\"scream\",\"screw\",\"scribble\",\"scrub\",\"seal\",\"search\",\"separate\",\"serve\",\"settle\",\"shade\",\"share\",\"shave\",\"shelter\",\"shiver\",\"shock\",\"shop\",\"shrug\",\"sigh\",\"sign\",\"signal\",\"sin\",\"sip\",\"ski\",\"skip\",\"slap\",\"slip\",\"slow\",\"smash\",\"smell\",\"smile\",\"smoke\",\"snatch\",\"sneeze\",\"sniff\",\"snore\",\"snow\",\"soak\",\"soothe\",\"sound\",\"spare\",\"spark\",\"sparkle\",\"spell\",\"spill\",\"spoil\",\"spot\",\"spray\",\"sprout\",\"squash\",\"squeak\",\"squeal\",\"squeeze\",\"stain\",\"stamp\",\"stare\",\"start\",\"stay\",\"steer\",\"step\",\"stir\",\"stitch\",\"stop\",\"store\",\"strap\",\"strengthen\",\"stretch\",\"strip\",\"stroke\",\"stuff\",\"subtract\",\"succeed\",\"suck\",\"suffer\",\"suggest\",\"suit\",\"supply\",\"support\",\"suppose\",\"surprise\",\"surround\",\"suspect\",\"suspend\",\"switch\",\"talk\",\"tame\",\"tap\",\"taste\",\"tease\",\"telephone\",\"tempt\",\"terrify\",\"test\",\"thank\",\"thaw\",\"tick\",\"tickle\",\"tie\",\"time\",\"tip\",\"tire\",\"touch\",\"tour\",\"tow\",\"trace\",\"trade\",\"train\",\"transport\",\"trap\",\"travel\",\"treat\",\"tremble\",\"trick\",\"trip\",\"trot\",\"trouble\",\"trust\",\"try\",\"tug\",\"tumble\",\"turn\",\"twist\",\"type\",\"undress\",\"unfasten\",\"unite\",\"unlock\",\"unpack\",\"untidy\",\"use\",\"vanish\",\"visit\",\"wail\",\"wait\",\"walk\",\"wander\",\"want\",\"warm\",\"warn\",\"wash\",\"waste\",\"watch\",\"water\",\"wave\",\"weigh\",\"welcome\",\"whine\",\"whip\",\"whirl\",\"whisper\",\"whistle\",\"wink\",\"wipe\",\"wish\",\"wobble\",\"wonder\",\"work\",\"worry\",\"wrap\",\"wreck\",\"wrestle\",\"wriggle\",\"x-ray\",\"yawn\",\"yell\",\"zip\",\"zoom\"]\n"
      ],
      "metadata": {
        "id": "DYe56E5Yywbl"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import string\n",
        "import random\n",
        "def get_valid(words):\n",
        "  word = random.choice(words)\n",
        "#this while loop we check the random string has space or -\n",
        "  while '-'in word or ' ' in word:\n",
        "    word = random.choice(words)\n",
        "  return word\n",
        "\n",
        "\n",
        "def hangman():\n",
        "  word = get_valid(words).upper()\n",
        "  word_letters = set(word)\n",
        "  print(word)\n",
        "  alphabet = set(string.ascii_uppercase)\n",
        "  used_letters = set()\n",
        "  while len(word_letters) > 0:\n",
        "    print(\"you have used these letters: \", ' ' .join(used_letters))\n",
        "    word_list = [letter if letter in used_letters else '-'for letter in word]\n",
        "    print('current word',' '.join(word_list))\n",
        "    user_letter = input('Guess a letter: ').upper()\n",
        "    if user_letter in alphabet - used_letters:\n",
        "      used_letters.add(user_letter)\n",
        "      if user_letter in word_letters:\n",
        "        word_letters.remove(user_letter)\n",
        "    elif user_letter in used_letters:\n",
        "      print('you have already used that choice')\n",
        "\n",
        "    else:\n",
        "      print(\"invalid charactors . please try again \")\n",
        "  print('current word',' '.join(word_list))\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "ZgLfyB0czC2Z"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "rt\n",
        "hangman()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xuZpXwGcz73D",
        "outputId": "8d9634ea-6649-4f77-a11f-efceb2c07498"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "UNDERSTOOD\n",
            "you have used these letters:  \n",
            "current word - - - - - - - - - -\n",
            "Guess a letter: u\n",
            "you have used these letters:  U\n",
            "current word U - - - - - - - - -\n",
            "Guess a letter: n\n",
            "you have used these letters:  N U\n",
            "current word U N - - - - - - - -\n",
            "Guess a letter: f\n",
            "you have used these letters:  F N U\n",
            "current word U N - - - - - - - -\n",
            "Guess a letter: d\n",
            "you have used these letters:  F D N U\n",
            "current word U N D - - - - - - D\n",
            "Guess a letter: e\n",
            "you have used these letters:  E D U N F\n",
            "current word U N D E - - - - - D\n",
            "Guess a letter: r\n",
            "you have used these letters:  E D U N R F\n",
            "current word U N D E R - - - - D\n",
            "Guess a letter: s\n",
            "you have used these letters:  E S D U N R F\n",
            "current word U N D E R S - - - D\n",
            "Guess a letter: r\n",
            "you have already used that choice\n",
            "you have used these letters:  E S D U N R F\n",
            "current word U N D E R S - - - D\n",
            "Guess a letter: a\n",
            "you have used these letters:  E S D U A N R F\n",
            "current word U N D E R S - - - D\n",
            "Guess a letter: t\n",
            "you have used these letters:  E S T D U A N R F\n",
            "current word U N D E R S T - - D\n",
            "Guess a letter: a\n",
            "you have already used that choice\n",
            "you have used these letters:  E S T D U A N R F\n",
            "current word U N D E R S T - - D\n",
            "Guess a letter: a\n",
            "you have already used that choice\n",
            "you have used these letters:  E S T D U A N R F\n",
            "current word U N D E R S T - - D\n",
            "Guess a letter: o\n",
            "current word U N D E R S T - - D\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "word=random.choice(words)\n",
        "print(word)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pNpphm5Jz-EI",
        "outputId": "ed790cec-2c96-4818-b23d-0978e77ec14b"
      },
      "execution_count": 85,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "crawl\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "new = [\"words\", \"to add\", \"new-word\",\"newWord\"]"
      ],
      "metadata": {
        "id": "Y7Lzuc4p0Etj"
      },
      "execution_count": 77,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "def singleWOrd(listofword):\n",
        "  word = random.choice(listofword)\n",
        "\n",
        "  while '-'in word or ' ' in word:\n",
        "      word = random.choice(listofword)\n",
        "  return word\n",
        ""
      ],
      "metadata": {
        "id": "iIanLKjE0For"
      },
      "execution_count": 97,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import string\n",
        "def hangman():\n",
        "  word=singleWOrd(new).upper()\n",
        "  setofword = set(word)\n",
        "  alpha = set(string.ascii_uppercase)\n",
        "\n",
        "  print(alpha)\n",
        "\n"
      ],
      "metadata": {
        "id": "6c1qXFKCSwO0"
      },
      "execution_count": 113,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "used_letter = set()"
      ],
      "metadata": {
        "id": "QJDevpbeXSOm"
      },
      "execution_count": 142,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "alpha = set(string.ascii_uppercase)\n",
        "word =singleWOrd(new)\n",
        "length = len(word)\n",
        "while length + 1 > 0:\n",
        "\n",
        "  inputvalkues= input(\"enter you letter \")\n",
        "  print(\"you have used these letters: \" , ' ' .join(inputvalkuesd))\n",
        "  word_list = [letter if letter in used_letter else '-'for letter in word]\n",
        "\n",
        "  print(word_list)\n",
        "  if inputvalkues in alpha - used_letter:\n",
        "      used_letter.add(inputvalkues)\n",
        "  length -1\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 917
        },
        "id": "1WRlz7QmXT9B",
        "outputId": "32d52c9d-f069-45ef-a49d-095b34870c9f"
      },
      "execution_count": 150,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "enter you letter o\n",
            "you have used these letters:  o\n",
            "['-', '-', '-', '-', '-']\n",
            "enter you letter a\n",
            "you have used these letters:  a\n",
            "['-', '-', '-', '-', '-']\n",
            "enter you letter s\n",
            "you have used these letters:  s\n",
            "['-', '-', '-', '-', '-']\n",
            "enter you letter d\n",
            "you have used these letters:  d\n",
            "['-', '-', '-', '-', '-']\n",
            "enter you letter r\n",
            "you have used these letters:  r\n",
            "['-', '-', '-', '-', '-']\n",
            "enter you letter f\n",
            "you have used these letters:  f\n",
            "['-', '-', '-', '-', '-']\n",
            "enter you letter df\n",
            "you have used these letters:  d f\n",
            "['-', '-', '-', '-', '-']\n",
            "enter you letter f\n",
            "you have used these letters:  f\n",
            "['-', '-', '-', '-', '-']\n",
            "enter you letter f\n",
            "you have used these letters:  f\n",
            "['-', '-', '-', '-', '-']\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-150-50c01be05dfb>\u001b[0m in \u001b[0;36m<cell line: 4>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mwhile\u001b[0m \u001b[0mlength\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0;36m1\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m   \u001b[0minputvalkues\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"enter you letter \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m   \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"you have used these letters: \"\u001b[0m \u001b[0;34m,\u001b[0m \u001b[0;34m' '\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0mjoin\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minputvalkues\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m   \u001b[0mword_list\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mletter\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mletter\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mused_letter\u001b[0m \u001b[0;32melse\u001b[0m \u001b[0;34m'-'\u001b[0m\u001b[0;32mfor\u001b[0m \u001b[0mletter\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mword\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def addQuantity(num1,num2):\n",
        "  print (f\"total value is : {num1+num2}\")"
      ],
      "metadata": {
        "id": "bOwgLo01e20r"
      },
      "execution_count": 160,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def addtowelemet(num1,num2):\n",
        "  print(num1+num2)\n",
        "  return (num1+num2)"
      ],
      "metadata": {
        "id": "V6sqTtaxfMr1"
      },
      "execution_count": 163,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(addtowelemet(5,4))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pFXffO_qfOLM",
        "outputId": "2edec24a-5076-4784-aac8-ae92e9401580"
      },
      "execution_count": 168,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "metadata": {},
          "execution_count": 168
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(addQuantity(2,3))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LIeACJdbgE4v",
        "outputId": "b0cbd0cc-02f7-4af7-b5b6-f9531c81a7a1"
      },
      "execution_count": 170,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "total value is : 5\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "NoneType"
            ]
          },
          "metadata": {},
          "execution_count": 170
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def bonace (*num):\n",
        "  list=[]\n",
        "  for i in num :\n",
        "    for x in i :\n",
        "      print(x*2)\n",
        "  return(i)\n",
        "\n",
        "salary ={\n",
        "\n",
        "         \"d\":20 ,\n",
        "         \"f\":10,\n",
        "         \"g\":30,\n",
        "         \"i\":100,\n",
        "\n",
        "}\n",
        "\n",
        "bonace(list(salary.values()))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "u_PhS-4IgnDP",
        "outputId": "35e88987-7f47-4b3b-a99e-7f194e07a2ea"
      },
      "execution_count": 234,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "40\n",
            "20\n",
            "60\n",
            "200\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[20, 10, 30, 100]"
            ]
          },
          "metadata": {},
          "execution_count": 234
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "list(salary.values())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kWbPJQL0wjHX",
        "outputId": "bf98cc5d-bed9-4db4-8086-43829856b500"
      },
      "execution_count": 224,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[20, 10, 30, 100]"
            ]
          },
          "metadata": {},
          "execution_count": 224
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cal(1,2,3,4,5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0ImFDj0alzlJ",
        "outputId": "ef051bed-c52c-4973-c5b3-5ea321dc73a5"
      },
      "execution_count": 176,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "4\n",
            "9\n",
            "16\n",
            "25\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def mess():\n",
        "\n",
        "  message= \"hello world\"\n",
        "  print(message)\n",
        "mess()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wVmRKJZel1XI",
        "outputId": "d05be4e6-d994-409a-b69f-a8efbf9ca14e"
      },
      "execution_count": 186,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello world\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "message = \"new message\""
      ],
      "metadata": {
        "id": "DhL3bpnVpTBs"
      },
      "execution_count": 187,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x=30\n",
        "def calculate_num():\n",
        "  x=20\n",
        "  print(x)\n",
        "calculate_num()\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8YIi4d_XpVlC",
        "outputId": "18def938-f1d1-4ea8-d648-8ebc03cc0c09"
      },
      "execution_count": 192,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20\n",
            "30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x=30\n",
        "def calculate_num():\n",
        "  global x\n",
        "  x=20\n",
        "  print(x)\n",
        "calculate_num()\n",
        "\n",
        "print(\"global value:\" ,x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J7WNjcNnp3td",
        "outputId": "8832bb7d-4235-4f15-ae8f-160be97da320"
      },
      "execution_count": 194,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20\n",
            "global value: 20\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "range(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PjD-dEkQseSn",
        "outputId": "4d888210-732a-4910-e9d4-8de9e9ce7991"
      },
      "execution_count": 235,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "range(0, 5)"
            ]
          },
          "metadata": {},
          "execution_count": 235
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in  range(5):\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Pi-7H5bgyra0",
        "outputId": "2f14af4c-c8a4-4276-ddb6-7e369bcab3b2"
      },
      "execution_count": 238,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "salary = {'d':{\"A\":32, \"b\": 20}, \"z\":{'f': 10, \"ss\":32}, 'g':{\"z\": 30,'i': 100}}\n"
      ],
      "metadata": {
        "id": "6XHWR8n0yuPV"
      },
      "execution_count": 257,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for i ,(x,z)  in enumerate(salary.items()):\n",
        "  print(f\" outside loop index {i}\")\n",
        "  for b,  (c,j) in enumerate(z.items()) :\n",
        "    print(f\" index : {b} and and value :{c}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZRoHfSAR1bSG",
        "outputId": "391be999-022a-447b-ce5f-ee70c5a9b725"
      },
      "execution_count": 264,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " outside loop index 0\n",
            " index : 0 and and value :A\n",
            " index : 1 and and value :b\n",
            " outside loop index 1\n",
            " index : 0 and and value :f\n",
            " index : 1 and and value :ss\n",
            " outside loop index 2\n",
            " index : 0 and and value :z\n",
            " index : 1 and and value :i\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "BFBhFPUj1gEG"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}