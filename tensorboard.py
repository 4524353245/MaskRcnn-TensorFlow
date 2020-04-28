from tensorboard.backend.event_processing import event_accumulator
import matplotlib.pyplot as plt
 
def read_tensorboard_data(tensorboard_path, val_name):
    """读取tensorboard数据，
    tensorboard_path是tensorboard数据地址val_name是需要读取的变量名称"""
    ea = event_accumulator.EventAccumulator(tensorboard_path)
    ea.Reload()
    print(ea.scalars.Keys())
    val = ea.scalars.Items(val_name)
    return val
 
def draw_plt(val, val_name):
    """将数据绘制成曲线图，val是数据，val_name是变量名称"""
    plt.figure()
    plt.plot([i.step for i in val], [j.value for j in val], label=val_name)
    """横坐标是step，迭代次数
    纵坐标是变量值"""
    plt.xlabel('step')
    plt.ylabel(val_name)
    plt.show()
 
if __name__ == "__main__":
    tensorboard_path = 'C:\\Users\\surface\\Desktop\\events.out.tfevents.1587948144.799453ecc049'
    val_name = 'loss'
    val = read_tensorboard_data(tensorboard_path, val_name)
    draw_plt(val, val_name)