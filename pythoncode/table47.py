import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 数据准备
attack_types = ['Type 1', 'Type 2', 'Type 4', 'Type 8', 'Type 16', 'Avg']
dr_values = [97.8, 91.3, 99.1, 88.6, 93.5, 94.1]  # 检测率
fpr_values = [1.5, 3.8, 0.9, 5.1, 2.7, 2.8]      # 误报率
f1_values = [98.1, 93.4, 99.2, 91.3, 95.1, 95.4] # F1分数（转换为百分比）

# 创建图形
fig, ax = plt.subplots(figsize=(12, 7))

# 设置柱状图位置和宽度
x = np.arange(len(attack_types))
width = 0.25

# 绘制三个指标的柱状图（交换了第二个和第三个柱子的位置）
bars1 = ax.bar(x - width, dr_values, width, label='检测率 (DR)', color='#2E8B57', alpha=0.8)
bars2 = ax.bar(x, f1_values, width, label='F1分数', color='#4169E1', alpha=0.8)  # 原来第三个柱子
bars3 = ax.bar(x + width, fpr_values, width, label='误报率 (FPR)', color='#CD5C5C', alpha=0.8)  # 原来第二个柱子

# 设置图表标题和标签
ax.set_xlabel('攻击类型', fontsize=12, fontweight='bold')
ax.set_ylabel('百分比 (%)', fontsize=12, fontweight='bold')
ax.set_title('SAFL-VR对不同攻击类型的检测性能', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(attack_types, fontsize=10)

# 添加图例
ax.legend(loc='upper right', framealpha=0.9)

# 在柱子上方添加数值标签
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 垂直偏移
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

add_value_labels(bars1)
add_value_labels(bars2)
add_value_labels(bars3)

# # 添加检测难度标注
# difficulty_labels = ['中等', '较高', '低', '高', '中等', '-']
# for i, label in enumerate(difficulty_labels):
#     ax.text(x[i], -5, f'难度: {label}', ha='center', va='top', fontsize=9,
#             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray", alpha=0.7))

# 设置y轴范围
ax.set_ylim(0, 105)

# 添加网格线
ax.grid(axis='y', alpha=0.3, linestyle='--')

# 调整布局
plt.tight_layout()

# 保存图片
plt.savefig('attack_type_performance.png', dpi=300, bbox_inches='tight')
plt.savefig('attack_type_performance.pdf', bbox_inches='tight')

# 显示图表
plt.show()

# 打印数据统计
print("="*50)
print("攻击类型检测性能统计:")
print("="*50)
for i, atk_type in enumerate(attack_types):
    print(f"{atk_type}: DR={dr_values[i]}%, FPR={fpr_values[i]}%, F1={f1_values[i]}%")