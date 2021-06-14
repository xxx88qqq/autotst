#include "subwidget.h"
#include "ui_subwidget.h"

subwidget::subwidget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::subwidget)
{
    ui->setupUi(this);
}

subwidget::~subwidget()
{
    delete ui;
}

void subwidget::on_buttonBox_clicked(QAbstractButton *button)
{
    this->destroy();
}
