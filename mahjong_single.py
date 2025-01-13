"""
程序名称：麻将游戏（单机）
（2024秋计算概论B大作业——麻将）
作者：侯佳奇
日期：2025年1月3日

使用方法：直接运行程序，按照提示进行操作。
"""

import random
import os  # 导入 os 模块，用于清屏

class MahjongGame:
    """麻将游戏主类，管理游戏的初始化、玩家操作和游戏流程。"""

    def __init__(self):
        """
        初始化游戏，包括牌堆、玩家信息和当前玩家。
        """
        self.deck = self.initialize_deck()
        self.players = {
            i: {'hand': [], 'sub_hand': [], 'discards': [], 'draw': ''}
            for i in range(4)
        }
        self.current_player = 0
        self.initialize_hands()

    def initialize_deck(self):
        """
        创建并洗牌牌堆，包括三种花色，每种数字1-9各四张。
        """
        suits = ['S', 'M', 'P']
        deck = [
            f"{suit}{num}"
            for suit in suits
            for num in range(1, 10)
            for _ in range(4)
        ]
        random.shuffle(deck)
        return deck

    def initialize_hands(self):
        """
        为每个玩家发牌，每人13张。
        """
        for i in range(4):
            self.players[i]['hand'] = [self.deck.pop() for _ in range(13)]
            self.players[i]['hand'] = self.sort_tiles(self.players[i]['hand'])
    
    def clear_screen(self):
        """
        清屏操作，不同系统使用不同命令。
        """
        os.system('cls')  # 清屏，Windows系统使用 'cls'，Linux或Mac使用 'clear'

    def sort_tiles(self, tiles):
        """
        对手牌进行排序，按花色和数字排序。
        """
        suit_order = {'S': 0, 'M': 1, 'P': 2}
        return sorted(tiles, key=lambda x: (suit_order[x[0]], int(x[1:])))

    def display_info(self):
        """
        显示当前玩家的信息，包括手牌、副露、剩余牌数等。
        """
        sorted_hand = self.sort_tiles(self.players[0]['hand'])
        if self.players[0]['draw']:
            sorted_hand_with_draw = self.sort_tiles(sorted_hand + [self.players[0]['draw']])
            hand_display = f"{sorted_hand_with_draw}"
        else:
            hand_display = f"{sorted_hand}"
        print(f"用户ID: 0")
        print(f"当前玩家ID: {self.current_player}")
        print(f"用户手牌: {hand_display}")
        print(f"用户副露: {self.players[0]['sub_hand']}")
        print(f"剩余牌数: {len(self.deck)}\n")

    def draw_tile(self, player_id):
        """
        玩家摸牌，如果牌堆不为空，返回摸到的牌，否则返回 None。
        """
        if self.deck:
            tile = self.deck.pop()
            # 只有在没有进行吃碰杠操作时才添加摸牌
            if not self.players[player_id]['sub_hand'] or len(self.players[player_id]['hand']) <= 13:
                self.players[player_id]['draw'] = tile
                self.players[player_id]['hand'].append(tile)
            return tile
        return None

    def discard_tile(self, player_id, tile):
        """
        玩家弃牌，将指定的牌从手牌中移除并加入弃牌堆。
        """
        if tile in self.players[player_id]['hand']:
            self.players[player_id]['hand'].remove(tile)
            self.players[player_id]['draw'] = ''
            self.players[player_id]['discards'].append(tile)
            print(f"玩家{player_id}打出了{tile}")
        else:
            print(f"玩家{player_id}没有这张牌 {tile}")
            if player_id == 0:
                self.player_discard(player_id)
            else:
                discard_tile = random.choice(self.players[player_id]['hand'])
                self.discard_tile(player_id, discard_tile)
            return

        input("按回车键继续...")
        self.clear_screen()
        self.display_info()
        self.check_actions(player_id, tile)

    def player_discard(self, player_id):
        """
        处理玩家的弃牌操作，允许玩家选择要弃掉的牌。
        """
        while True:
            print("请选择你需要切出的牌 (直接按回车可切出刚摸到的牌):")
            discard_tile = input().strip()
            
            # 如果直接回车，弃掉刚摸到的牌
            if discard_tile == '' and self.players[player_id]['draw']:
                tile = self.players[player_id]['draw']
                self.discard_tile(player_id, tile)
                break
            # 检查是否在手牌或是刚摸到的牌
            elif discard_tile in self.players[player_id]['hand'] or discard_tile == self.players[player_id]['draw']:
                self.discard_tile(player_id, discard_tile)
                break
            else:
                print(f"无效的输入: {discard_tile}")
                print("请从你的手牌中选择一张牌")
                sorted_hand = self.sort_tiles(self.players[player_id]['hand'])
                draw_tile = self.players[player_id]['draw']
                if draw_tile:
                    print(f"当前手牌: {sorted_hand} + [{draw_tile}](刚摸到的牌)")
                else:
                    print(f"当前手牌: {sorted_hand}")
    
    def user_turn(self):
        """
        处理用户的回合，包括摸牌、选择操作和执行操作。
        """
        self.clear_screen()
        self.display_info()
        tile = self.draw_tile(0)
        print(f"您摸到了: {tile}")
        
        while True:
            available_actions = self.get_available_actions(0)
            action = input(f"请输入操作 {available_actions}: ")
            
            if action == '0' and '0:胡牌' in available_actions:
                print("您胡牌了！")
                self.end_game(0)
                return
            elif action == '1': 
                self.player_discard(0)
                break
            elif action == '2':
                self.clear_screen()
                self.display_info()
                self.query()
                self.clear_screen()
                self.display_info()
            elif action == '3' and '3:暗杠' in available_actions:
                self.gang0(0)
                break
            elif action == '4' and '4:补杠' in available_actions:
                self.gang2(0)
                break
            else:
                print("无效的操作，请重新输入。")
        # 不在这里更新 current_player
        # 让 play_game 负责更新

    def get_available_actions(self, player_id):
        """
        获取当前玩家可执行的操作列表。
        """
        actions = []
        if self.can_hu(player_id):
            actions.append('0:胡牌')
        actions.append('1:弃牌')
        actions.append('2:查询')
        if self.can_gang0(player_id):
            actions.append('3:暗杠')
        if self.can_gang2(player_id):
            actions.append('4:补杠')
        return actions

    def can_hu(self, player_id):
        """
        判断玩家是否可以自摸胡牌。
        """
        tiles = self.players[player_id]['hand'].copy()
        tiles = self.sort_tiles(tiles)
        # 如果有副露，需要考虑副露的影响
        sub_hand = self.players[player_id]['sub_hand']
        if sub_hand:
            # 计算还需要多少组合
            remaining_groups = (14 - len(tiles)) // 3
            if remaining_groups == len(sub_hand):  # 确认副露数量正确
                return self.is_valid_hand(tiles)
        else:
            return self.is_valid_hand(tiles)
        return False

    def is_valid_hand(self, tiles):
        """
        判断手牌是否构成有效的胡牌型。
        """
        if len(tiles) % 3 != 2:  # 首先确认牌数是否符合3n+2
            return False
            
        # 对牌进行计数
        tile_count = {}
        for tile in tiles:
            tile_count[tile] = tile_count.get(tile, 0) + 1
            
        # 尝试每一种可能的对子
        for tile in tile_count:
            if tile_count[tile] >= 2:
                # 复制牌的统计信息
                temp_count = tile_count.copy()
                # 移除对子
                temp_count[tile] -= 2
                if temp_count[tile] == 0:
                    del temp_count[tile]
                
                # 检查剩余牌是否能组成顺子或刻子
                if self.can_form_complete_hand(temp_count):
                    return True
        return False

    def can_form_complete_hand(self, tile_count):
        """
        检查剩余牌是否能组成完整的顺子和刻子组合。
        """
        if not tile_count:  # 如果没有剩余牌，说明组合成功
            return True
            
        # 获取任意一张牌开始尝试
        tile = list(tile_count.keys())[0]
        
        # 尝试组成刻子
        if tile_count[tile] >= 3:
            temp_count = tile_count.copy()
            temp_count[tile] -= 3
            if temp_count[tile] == 0:
                del temp_count[tile]
            if self.can_form_complete_hand(temp_count):
                return True
                
        # 尝试组成顺子
        if tile[0] in ['S', 'M', 'P'] and tile[1:].isdigit():
            suit, num = tile[0], int(tile[1:])
            if num <= 7:  # 确保能组成顺子
                second = f"{suit}{num+1}"
                third = f"{suit}{num+2}"
                if (second in tile_count and third in tile_count and
                    tile_count[tile] > 0 and 
                    tile_count[second] > 0 and 
                    tile_count[third] > 0):
                    temp_count = tile_count.copy()
                    temp_count[tile] -= 1
                    temp_count[second] -= 1
                    temp_count[third] -= 1
                    # 清理计数为0的牌
                    for t in [tile, second, third]:
                        if temp_count[t] == 0:
                            del temp_count[t]
                    if self.can_form_complete_hand(temp_count):
                        return True
        
        return False

    ###以上部分全是胡牌相关算法

    def can_gang0(self, player_id):
        """
        判断玩家是否可以进行暗杠。
        """
        hand = self.players[player_id]['hand']
        for tile in set(hand):
            if hand.count(tile) == 4:
                return True
        return False

    def can_gang2(self, player_id):
        """
        判断玩家是否可以进行补杠。
        """
        hand = self.players[player_id]['hand']
        sub_hand = self.players[player_id]['sub_hand']
        for meld in sub_hand:
            if len(meld) == 3 and meld.count(meld[0]) == 3 and meld[0] in hand:
                return True
        return False

    def query(self):
        """
        处理玩家的查询操作，允许查看其他玩家的弃牌和副露。
        """
        while True:
            query_action = input("输入查询指令 (1:查看弃牌 2:查看副露) 或输入'Exit'退出查询: ")
            if query_action.lower() == 'exit':
                break
            elif query_action.startswith('1:'):
                try:
                    player_id = int(query_action.split(':')[1])
                    print(f"玩家{player_id}的弃牌: {self.players[player_id]['discards']}")
                except (IndexError, ValueError):
                    print("无效的玩家ID。")
            elif query_action.startswith('2:'):
                try:
                    player_id = int(query_action.split(':')[1])
                    print(f"玩家{player_id}的副露: {self.players[player_id]['sub_hand']}")
                except (IndexError, ValueError):
                    print("无效的玩家ID。")
            else:
                print("无效的查询指令，请重新输入。")

    def end_game(self, winner_id):
        """
        结束游戏，显示最终结果并退出程序。
        """
        self.clear_screen()
        print(f"玩家{winner_id}获胜！")
        for i in range(4):
            sorted_hand = self.sort_tiles(self.players[i]['hand'])
            print(f"玩家{i}的手牌: {sorted_hand}")
            print(f"玩家{i}的副露: {self.players[i]['sub_hand']}")
            print(f"玩家{i}的弃牌: {self.players[i]['discards']}")
        exit()

    def play_game(self):
        """
        主游戏循环，控制游戏的进行，直到牌堆为空或有玩家胡牌。
        """
        while self.deck:
            if self.current_player == 0:
                self.user_turn()
            else:
                self.computer_turn(self.current_player)
            # 更新 current_player 只在这里进行
            self.current_player = (self.current_player + 1) % 4
        self.clear_screen()
        print("牌堆已空，游戏结束。")
        for i in range(4):
            sorted_hand = self.sort_tiles(self.players[i]['hand'])
            print(f"玩家{i}的手牌: {sorted_hand}")
            print(f"玩家{i}的副露: {self.players[i]['sub_hand']}")
            print(f"玩家{i}的弃牌: {self.players[i]['discards']}")

    def computer_turn(self, player_id):
        """
        处理电脑玩家的回合，包括摸牌和弃牌操作。
        """
        self.clear_screen()
        self.display_info()
        tile = self.draw_tile(player_id)
        
        # 检查是否可以胡牌
        if self.can_hu(player_id):
            print(f"玩家{player_id}胡牌了！")
            self.end_game(player_id)
            return
        
        # 确保玩家手牌不为空
        if self.players[player_id]['hand']:
            discard_tile = random.choice(self.players[player_id]['hand'])
            self.discard_tile(player_id, discard_tile)

    def check_actions(self, player_id, tile):
        """
        检查并处理其他玩家对打出的牌的响应，如胡、碰、吃。
        """
        # 依次检查所有玩家（按逆时针顺序）
        for i in range(1, 4):
            next_player = (player_id + i) % 4
            if next_player == player_id:
                continue
                
            # 收集所有可用操作
            available_actions = []
            if self.can_hu_by_tile(next_player, tile):
                available_actions.append('0:胡牌')
            if self.can_chi(next_player, tile) and next_player == (player_id + 1) % 4:
                available_actions.append('1:吃牌')
            if self.can_peng(next_player, tile):
                available_actions.append('2:碰牌')
            if self.can_gang1(next_player, tile):
                available_actions.append('3:明杠')
            
            if available_actions:
                available_actions.append('4:忽略')
                if next_player == 0:  # 人类玩家
                    self.clear_screen()
                    self.display_info()
                    print(f"\n玩家{player_id}打出了：{tile}")
                    print("-" * 30)
                    print("请选择操作：")
                    print("0:胡牌, 1:吃牌, 2:碰牌, 3:明杠, 4:忽略")
                    print("-" * 30)
                    
                    while True:
                        action = input("请输入操作编号(0-4): ").strip()
                        if action == '0' and '0:胡牌' in available_actions:
                            self.end_game(0)
                            return True
                        elif action == '1' and '1:吃牌' in available_actions:
                            if self.chi(0, player_id, tile):
                                self.current_player = 0
                                return True
                        elif action == '2' and '2:碰牌' in available_actions:
                            self.peng(0, player_id, tile)
                            self.current_player = 0
                            return True
                        elif action == '3' and '3:明杠' in available_actions:
                            self.gang1(0, player_id, tile)
                            self.turn_after_gang(0)
                            return True
                        elif action == '4':
                            break
                        else:
                            print("无效的操作，请重新输入。")
                
                else:  # AI玩家
                    if '0:胡牌' in available_actions:
                        print(f"玩家{next_player}选择了胡牌")
                        self.end_game(next_player)
                        return True
                    # AI随机选择其他操作
                    if random.random() < 0.5:  # 50%概率执行操作
                        if '3:明杠' in available_actions:
                            print(f"玩家{next_player}选择了明杠")
                            self.gang1(next_player, player_id, tile)
                            self.turn_after_gang(next_player)
                            return True
                        elif '2:碰牌' in available_actions:
                            print(f"玩家{next_player}选择了碰牌")
                            self.peng(next_player, player_id, tile)
                            self.current_player = next_player
                            return True
                        elif '1:吃牌' in available_actions:
                            print(f"玩家{next_player}选择了吃牌")
                            if self.chi(next_player, player_id, tile):
                                self.current_player = next_player
                                return True
            
        return False

    def can_hu_by_tile(self, player_id, tile):
        """
        判断玩家是否可以点炮胡牌。
        """
        tiles = self.players[player_id]['hand'].copy()
        tiles.append(tile)
        tiles = self.sort_tiles(tiles)
        # 考虑副露的情况
        sub_hand = self.players[player_id]['sub_hand']
        if sub_hand:
            # 计算还需要多少组合
            remaining_groups = (14 - len(tiles)) // 3
            if remaining_groups == len(sub_hand):  # 确认副露数量正确
                return self.is_valid_hand(tiles)
        else:
            return self.is_valid_hand(tiles)
        return False

    def can_peng(self, player_id, tile):
        """
        判断玩家是否可以碰牌。
        """
        return self.players[player_id]['hand'].count(tile) >= 2

    def can_gang1(self, player_id, tile):
        """
        判断玩家是否可以杠牌（补杠）。
        """
        return self.players[player_id]['hand'].count(tile) == 3

    def can_chi(self, player_id, tile):
        """
        检查玩家是否可以吃牌。
        """
        if not tile or len(tile) < 2:  # 添加输入验证
            return False
        
        hand = self.players[player_id]['hand']
        suit = tile[0]
        if not tile[1:].isdigit():
            return False
        num = int(tile[1:])
        sequences = [
            [f"{suit}{num-2}", f"{suit}{num-1}"],
            [f"{suit}{num-1}", f"{suit}{num+1}"],
            [f"{suit}{num+1}", f"{suit}{num+2}"]
        ]
        return any(all(t in hand for t in seq) for seq in sequences)

    def peng(self, player_id, from_player_id, tile):
        """
        执行碰牌操作，将指定的牌加入副露，并从手牌中移除相应的牌。
        """
        # 清空摸牌状态
        self.players[player_id]['draw'] = ''
        
        # 检查并移除手牌中的两张相同牌
        count = 0
        hand = self.players[player_id]['hand']
        temp_hand = hand.copy()
        for t in temp_hand:
            if t == tile and count < 2:
                hand.remove(t)
                count += 1
        
        # 添加到副露
        self.players[player_id]['sub_hand'].append([tile] * 3)
        
        print(f"\n玩家{player_id}碰了玩家{from_player_id}的 {tile}")
        print(f"移除的牌: {tile}, {tile}")
        print(f"形成的碰牌组合: [{tile}, {tile}, {tile}]")
        input("按回车键继续...")
        
        self.clear_screen()
        self.display_info()
        print(f"现在轮到玩家{player_id}出牌")
        
        if player_id == 0:
            print("请选择要打出的牌：")
            self.player_discard(player_id)
        else:
            if self.players[player_id]['hand']:
                discard_tile = random.choice(self.players[player_id]['hand'])
                self.discard_tile(player_id, discard_tile)
        
        self.current_player = player_id

    def chi(self, player_id, from_player_id, tile):
        """
        执行吃牌操作，将指定的牌加入副露，并从手牌中移除相应的牌。
        """
        # 清空摸牌状态
        self.players[player_id]['draw'] = ''
        
        hand = self.players[player_id]['hand']
        suit = tile[0]
        num = int(tile[1:])
        
        # 定义可能的吃牌组合
        sequences = []
        if num >= 3:
            sequences.append([f"{suit}{num-2}", f"{suit}{num-1}", tile])
        if num >= 2 and num <= 8:
            sequences.append([f"{suit}{num-1}", tile, f"{suit}{num+1}"])
        if num <= 7:
            sequences.append([tile, f"{suit}{num+1}", f"{suit}{num+2}"])

        # 过滤出可行的吃牌组合
        valid_sequences = []
        for seq in sequences:
            need_tiles = [t for t in seq if t != tile]
            if all(hand.count(t) >= seq.count(t) for t in need_tiles):
                valid_sequences.append(seq)
        
        if not valid_sequences:
            if player_id == 0:
                print(f"无法吃 {tile}")
            return False

        if player_id == 0:
            print("可选的顺子组合：")
            for i, seq in enumerate(valid_sequences):
                print(f"{i+1}: {' '.join(seq)}")
            print("请输入你要吃的顺子(请以空格分开)，或输入'n'取消:")
            choice = input().strip()

            if choice.lower() == 'n':
                        return False
                        
            chosen_tiles = choice.split()
            if len(chosen_tiles) != 3:
                print("输入无效，必须输入3张牌")
                return False
                
            # 验证输入的顺子是否合法
            if chosen_tiles not in valid_sequences:
                print("输入的顺子组合无效")
                return False
                
            # 移除用于吃牌的牌
            for t in chosen_tiles:
                if t != tile and t in hand:
                    hand.remove(t)

            # 添加吃牌组合到副露
            self.players[player_id]['sub_hand'].append(chosen_tiles)
            print(f"玩家{player_id}吃了玩家{from_player_id}的 {tile}")
            print(f"形成的吃牌组合: {' '.join(chosen_tiles)}")
            self.display_info()
            
            # 处理弃牌
            self.player_discard(player_id)
            return True
        else:
            # AI 玩家随机选择一个可行的顺子
            chosen_seq = random.choice(valid_sequences)
            for t in chosen_seq:
                if t != tile and t in hand:
                    hand.remove(t)
            self.players[player_id]['sub_hand'].append(chosen_seq)
            print(f"玩家{player_id}吃了玩家{from_player_id}的 {tile}")
            print(f"形成的吃牌组合: {' '.join(chosen_seq)}")
            self.display_info()
            
            # AI 随机弃牌
            if hand:
                discard_tile = random.choice(hand)
                self.discard_tile(player_id, discard_tile)
            return True

    def gang1(self, player_id, from_player_id, tile):
        """
        执行明杠操作，将指定的牌加入副露，并从手牌中移除相应的牌。
        """
        for _ in range(3):
            self.players[player_id]['hand'].remove(tile)
        self.players[player_id]['sub_hand'].append([tile] * 4)
        print(f"玩家{player_id}杠了玩家{from_player_id}的 {tile}")
        self.display_info()
        self.turn_after_gang(player_id)

    def gang0(self, player_id):
        """
        执行暗杠操作，将指定的牌加入副露，并从手牌中移除相应的牌。
        """
        hand = self.players[player_id]['hand']
        for tile in set(hand):
            if hand.count(tile) == 4:
                for _ in range(4):
                    hand.remove(tile)
                self.players[player_id]['sub_hand'].append([tile] * 4)
                print(f"玩家{player_id}进行了暗杠 {tile}")
                self.display_info()
                self.turn_after_gang(player_id)
                return True
        return False

    def gang2(self, player_id):
        """
        执行补杠操作，将指定的牌加入副露，并从手牌中移除相应的牌。
        """
        hand = self.players[player_id]['hand']
        sub_hand = self.players[player_id]['sub_hand']
        for meld in sub_hand:
            if len(meld) == 3 and meld.count(meld[0]) == 3 and meld[0] in hand:
                tile = meld[0]
                hand.remove(tile)
                meld.append(tile)
                print(f"玩家{player_id}进行了补杠 {tile}")
                self.display_info()
                self.turn_after_gang(player_id)
                return True
        return False

    def turn_after_gang(self, player_id):
        """
        执行动作后的回合处理，包含摸牌和选择操作。
        """
        # 杠后摸牌
        tile = self.draw_tile(player_id)
        if not tile:  # 如果牌堆已空
            print("牌堆已空，游戏结束")
            self.end_game(None)
            return
            
        print(f"玩家{player_id}杠后摸到了: {tile}")
        
        # 判断是否能胡
        if self.can_hu(player_id):
            if player_id == 0:
                action = input("是否胡牌？(y/n): ")
                if action.lower() == 'y':
                    self.end_game(player_id)
                    return
            else:  # AI玩家选择胡牌
                print(f"玩家{player_id}胡牌了！")
                self.end_game(player_id)
                return
        
        # 没有胡牌则需要打出一张牌
        if player_id == 0:
            self.player_discard(player_id)
        else:
            discard_tile = random.choice(self.players[player_id]['hand'])
            self.discard_tile(player_id, discard_tile)

    def turn_after_action(self, player_id):
        """
        执行动作后的回合处理，包含摸牌和选择操作。
        """
        self.clear_screen()
        self.display_info()
        tile = self.draw_tile(player_id)
        print(f"玩家{player_id}摸到了: {tile}")
        if player_id == 0:
            while True:
                available_actions = self.get_available_actions(player_id)
                action = input(f"请输入操作 {available_actions}: ")
                if action == '0' and '0:胡牌' in available_actions:
                    print(f"玩家{player_id}胡牌了！")
                    self.end_game(player_id)
                elif action.startswith('1:'):
                    discard_tile = action[2:].trip()
                    if discard_tile == '':
                        discard_tile = tile  # 弃掉刚摸到的牌
                    self.discard_tile(player_id, discard_tile)
                    break
                elif action == '1':  # 直接弃掉刚摸到的牌
                    self.discard_tile(player_id, tile)
                    break
                elif action == '2':
                    self.clear_screen()
                    self.display_info()
                    self.query()
                    self.clear_screen()
                    self.display_info()
                elif action == '3' and '3:暗杠' in available_actions:
                    self.gang0(player_id)
                    break
                elif action == '4' and '4:补杠' in available_actions:
                    self.gang2(player_id)
                    break
                else:
                    print("无效的操作，请重新输入。")
            input("按回车键继续...")
            # 不在这里更新 current_player
            # 让 play_game 负责更新
        else:
            if self.can_hu(player_id):
                print(f"玩家{player_id}胡牌了！")
                self.end_game(player_id)
                return
            discard_tile = random.choice(self.players[player_id]['hand'])
            self.discard_tile(player_id, discard_tile)
            # 不在这里更新 current_player
            # 让 play_game 负责更新

if __name__ == "__main__":
    game = MahjongGame()
    game.play_game() 