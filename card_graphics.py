def return_card(card,double,Op_Sys):
   rank,suit = card.split()

   card_graphics = {
      '2': {
         'not_double': [
            '╭─────────╮',
            f'│2   {suit}    │',
            '│         │',
            '│         │',
            '│         │',
            f'│    {suit}   2│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│           2 │',
           f'│ {suit}         {suit} │',
            '│ 2           │',
            '╰─────────────╯']},
      '3': {
         'not_double': [
            '╭─────────╮',
            f'│3   {suit}    │',
            '│         │',
            f'│    {suit}    │',
            '│         │',
            f'│    {suit}   3│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│           3 │',
            f'│ {suit}    {suit}    {suit} │',
            '│ 3           │',
            '╰─────────────╯']},
      '4': {
         'not_double': [
            '╭─────────╮',
            f'│4 {suit}   {suit}  │',
            '│         │',
            '│         │',
            '│         │',
            f'│  {suit}   {suit} 4│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit}     {suit} 4 │',
            f'│             │',
            f'│ 4 {suit}     {suit}   │',
            '╰─────────────╯']},
      '5': {
         'not_double': [
            '╭─────────╮',
            f'│5 {suit}   {suit}  │',
            '│         │',
            f'│    {suit}    │',
            '│         │',
            f'│  {suit}   {suit} 5│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit}     {suit} 5 │',
            f'│      {suit}      │',
            f'│ 5 {suit}     {suit}   │',
            '╰─────────────╯']},
      '6': {
         'not_double': [
            '╭─────────╮',
            f'│6 {suit}   {suit}  │',
            '│         │',
            f'│  {suit}   {suit}  │',
            '│         │',
            f'│  {suit}   {suit} 6│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit}  {suit}  {suit} 6 │',
            '│             │',
            f'│ 6 {suit}  {suit}  {suit}   │',
            '╰─────────────╯']},
      '7': {
         'not_double': [
            '╭─────────╮',
            f'│7 {suit}   {suit}  │',
            f'│    {suit}    │',
            f'│  {suit}   {suit}  │',
            '│         │',
            f'│  {suit}   {suit} 7│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit}  {suit}  {suit} 7 │',
            f'│       {suit}     │',
            f'│ 7 {suit}  {suit}  {suit}   │',
            '╰─────────────╯']},
      '8': {
         'not_double': [
            '╭─────────╮',
            f'│8 {suit}   {suit}  │',
            f'│    {suit}    │',
            f'│  {suit}   {suit}  │',
            f'│    {suit}    │',
            f'│  {suit}   {suit} 8│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit}  {suit}  {suit} 8 │',
            f'│    {suit}   {suit}    │',
            f'│ 8 {suit}  {suit}  {suit}   │',
            '╰─────────────╯']},
      '9': {
         'not_double': [
            '╭─────────╮',
            f'│9 {suit}   {suit}  │',
            f'│  {suit}   {suit}  │',
            f'│    {suit}    │',
            f'│  {suit}   {suit}  │',
            f'│  {suit}   {suit} 9│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            f'│   {suit} {suit} {suit} {suit} 9 │',
            f'│      {suit}      │',
            f'│ 9 {suit} {suit} {suit} {suit}   │',
            '╰─────────────╯']},
      '10': {
         'not_double': [
            '╭─────────╮',
            f'│10 {suit} {suit}   │',
            f'│  {suit} {suit} {suit}  │',
            '│         │',
            f'│  {suit} {suit} {suit}  │',
            f'│   {suit} {suit} 10│',
            '╰─────────╯'],
         'double': [
             '╭─────────────╮',
            f'│   {suit} {suit} {suit} {suit} 10│',
            f'│     {suit} {suit}     │',
            f'│10 {suit} {suit} {suit} {suit}   │',
            '╰─────────────╯']},
      'face': {
         'not_double': {
             'Windows': [
               '╭─────────╮',
               f'│{rank} ██▓▓██ │',
               f'│{suit} ▓▓▓▓▓▓ │',
               '│ ▓▓▓▓▓▓▓ │',
               f'│ ▓▓▓▓▓▓ {suit}│',
               f'│ ██▓▓██ {rank}│',
               '╰─────────╯'],
            'Linux': [
                '╭─────────╮',
               f'│{rank} ▓▓▒▒▓▓ │',
               f'│{suit} ░░░░░░ │',
               '│ ▒░░░░░▒ │',
               f'│ ░░░░░░ {suit}│',
               f'│ ▓▓▒▒▓▓ {rank}│',
               '╰─────────╯']},
        'double': {
            'Windows': [
                '╭─────────────╮',
               f'│  █▓▓▓▓▓▓█ {suit}{rank}│',
               '│  ▓▓▓▓▓▓▓▓▓  │',
               f'│{rank}{suit} █▓▓▓▓▓▓█  │',
               '╰─────────────╯'],
            'Linux': [
                '╭─────────────╮',
               f'│  ▓░░▒░░░▓ {suit}{rank}│',
               '│  ▒▒░░░░░▒▒  │',
               f'│{rank}{suit} ▓░░░▒░░▓  │',
               '╰─────────────╯']}},
      'A ♥': {
         'not_double': [
            '╭─────────╮',
            '│A  _ _   │',
            '│♥ ( V )  │',
            '│   \ /   │',
            '│    V   ♥│',
            '│        A│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│      ⌢  ♥ A │',
            '│    ≺   ⧼    │',
            '│ A ♥  ⌣      │',
            '╰─────────────╯']},
      'A ♦': {
         'not_double': [
            '╭─────────╮',
            '│A   ^    │',
            '│♦ /   \  │',
            '│  \   /  │',
            '│    v   ♦│',
            '│        A│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│      ^  ♦ A │',
            '│   <     >   │',
            '│ A ♦  ⌵      │',
            '╰─────────────╯']},
      'A ♠': {
         'not_double': [
            '╭─────────╮',
            '│A   ^    │',
            '│♠  / \   │',
            '│  (_._)  │',
            '│    |   ♠│',
            '│        A│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│      ⌢  ♠ A │',
            '│    ─│   >   │',
            '│ A ♠  ⌣      │',
            '╰─────────────╯']},
      'A ♣': {
         'not_double': [
            '╭─────────╮',
            '│A   _    │',
            '│♣  ( )   │',
            '│  (_\'_)  │',
            '│    |   ♣│',
            '│        A│',
            '╰─────────╯'],
         'double': [
            '╭─────────────╮',
            '│         ♣ A │',
            '│    ─8o      │',
            '│ A ♣         │',
            '╰─────────────╯']},
      'back side': {
         'not_double': {
             'Windows': [
               '╭─────────╮',
               '│▓▓▓▓▓▓▓▓▓│',
               '│▓▓▓▓▓▓▓▓▓│',
               '│▓▓▓▓▓▓▓▓▓│',
               '│▓▓▓▓▓▓▓▓▓│',
               '│▓▓▓▓▓▓▓▓▓│',
               '╰─────────╯'],
            'Linux': [
                '╭─────────╮',
                '│⚜ ☠ ⚜ ☠  │',
                '│ ☠ ⚜ ☠ ⚜ │',
                '│⚜ ☠ ⚜ ☠  │',
                '│ ☠ ⚜ ☠ ⚜ │',
                '│⚜ ☠ ⚜ ☠  │',
                '╰─────────╯']},
        'double': {
            'Windows': [
                '╭─────────────╮',
                '│▓▓▓▓▓▓▓▓▓▓▓▓▓│',
                '│▓▓▓▓▓▓▓▓▓▓▓▓▓│',
                '│▓▓▓▓▓▓▓▓▓▓▓▓▓│',
                '╰─────────────╯'],
            'Linux': [
                '╭─────────────╮',
                '│ ☠ ⚜ ☠ ⚜ ☠ ⚜ │',
                '│  ⚜ ☠ ⚜ ☠ ⚜  │',
                '│ ☠ ⚜ ☠ ⚜ ☠ ⚜ │',
                '╰─────────────╯']}},
      'shoe card': {
         'not_double': [
            '▗▄▄▄▄▄▄▄▄▄',
            '▐█████████',
            '▐█████████',
            '▐█████████',
            '▐█████████',
            '▐█████████',
            '▝▀▀▀▀▀▀▀▀▀'],
         'double': ['this card is not needed']}}
   
   if rank in card_graphics: #number Cards
       if double:
           return card_graphics[rank]['double']
       else:
           return card_graphics[rank]['not_double']
   elif card == 'back side': #Reverse Side
       if double:
           return card_graphics[card]['double'][Op_Sys]
       else:
           return card_graphics[card]['not_double'][Op_Sys]
   elif card in card_graphics: #Aces and Shoe Card
       if double:
           return card_graphics[card]['double']
       else:
           return card_graphics[card]['not_double']
   elif rank in ('J','Q','K'): #Face Cards
       if double:
           return card_graphics['face']['double'][Op_Sys]
       else:
           return card_graphics['face']['not_double'][Op_Sys]
   else: 
       if double:
           return [
      '╭─────────────╮',
      '│error        │',
      '│        error│',
      '│error        │',
      '╰─────────────╯']   
       else:
           return [
      '╭─────────╮',
      '│error    │',
      '│    error│',
      '│error    │',
      '│    error│',
      '│error    │',
      '╰─────────╯']
       
